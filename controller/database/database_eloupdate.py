from controller.database.database_abstract import DatabaseAbstract


class DatabaseEloupdate(DatabaseAbstract):
    def __init__(self, player1, player2):
        # updated def such that player2 stats are also updated with one function run
        self.ai_game = False

        self.user1 = player1
        if isinstance(player2, int):
            self.ai_game = True
            print("ai game detected")
            self.ai_difficulty = player2
            self.user2 = "guest"
        else:
            self.user2 = player2

        self.quer_eloupdate_win = "UPDATE player SET elo = elo + %s WHERE username = %s"
        self.quer_eloupdate_loss = "UPDATE player SET elo = elo - %s WHERE username = %s"
        self.quer_elo = "SELECT elo FROM player WHERE username = %s"
        self.quer_matchupdate = "UPDATE player SET matches = matches + %s WHERE username = %s"
        self.winner_change = 10
        self.loser_change = 10


        self.higher_elo_win = True
        self.winner = None
        self.loser = None

    def get_elo_dif(self, player1, player2, winner):
        self.user1 = player1
        self.user2 = player2

        if self.user1 != "guest":
            with self.my_connect.cursor(buffered=True) as cursor:
                cursor.execute(self.quer_elo, (self.user1,))
                result1_elo = cursor.fetchall()

            user1_elo = result1_elo[0][0]
            cursor.close()
        else:
            user1_elo = 1000

        if self.user2 != "guest":
            if not self.ai_game:
                with self.my_connect.cursor(buffered=True) as cursor2:
                    cursor2.execute(self.quer_elo, (self.user2,))
                    result2_elo = cursor2.fetchall()

                user2_elo = result2_elo[0][0]
                cursor2.close()

        else:
            if self.ai_game:
                if self.ai_difficulty == 2:
                    user2_elo = 1000
                    print("Ai elo considered: 1000")
                elif self.ai_difficulty == 3:
                    user2_elo = 1300
                    print("Ai elo considered: 1300")
                elif self.ai_difficulty == 4:
                    user2_elo = 1600
                    print("Ai elo considered: 1600")
                elif self.ai_difficulty == 5:
                    user2_elo = 2000
                    print("Ai elo considered: 2000")

            else:
                user2_elo = 1000

        if user1_elo > user2_elo:
            if self.user1 == winner:
                self.higher_elo_win = True
                print("Player 1 win having higher elo")
            elif self.user2 == winner:
                self.higher_elo_win = False
                print("Player two win having lower elo")
        elif user2_elo > user1_elo:
            if self.user1 == winner:
                self.higher_elo_win = False
                print("Player 1 win having lower elo")
            elif self.user2 == winner:
                self.higher_elo_win = True
                print("player 2 win having higher elo")
        x = user2_elo - user1_elo
        print('Elo difference is {}'.format(x))
        return abs(x)

    def elo_change(self, player1, player2, winner):
        difference = self.get_elo_dif(player1, player2, winner)
        if difference <= 150:
            self.winner_change = 10
            self.loser_change = 10
            print("Elo change is 10 for 10")
        elif 150 < difference <= 350 and self.higher_elo_win == True:
            self.winner_change = 5
            self.loser_change = 5
            print("Elo change is 5 for 5")
        elif 150 < difference <= 350 and self.higher_elo_win == False:
            self.winner_change = 15
            self.loser_change = 20
            print("Elo change is 15 for 20")
        elif difference > 350 and self.higher_elo_win == True:
            self.winner_change = 2
            self.loser_change = 4
            print("Elo change is 2 for 4")
        elif difference > 350 and self.higher_elo_win == False:
            self.winner_change = 20
            self.loser_change = 25
            print("Elo change is 20 for 25")

    def execute_query(self, winner):
        if winner == self.user1:
            self.winner = self.user1
            self.loser = self.user2
        else:
            self.winner = self.user2
            self.loser = self.user1

        self.elo_change(self.user1, self.user2, winner)
        with self.my_connect.cursor() as cursor:
            if self.winner != "guest":
                cursor.execute(self.quer_eloupdate_win, (self.winner_change, self.winner))
                cursor.execute(self.quer_matchupdate, (1, self.winner))
                print('{} elo updated by {} as winner'.format(self.winner, self.winner_change))
            if self.loser != "guest":
                cursor.execute(self.quer_eloupdate_loss, (self.loser_change, self.loser))
                cursor.execute(self.quer_matchupdate, (1, self.loser))
                print('{} elo updated by {} as loser'.format(self.loser, self.loser_change))
            self.my_connect.commit()