Create Database if not exists reversi;
use reversi;

Create Table player(
    username varchar(32) primary key not null,
    password varchar(32) not null,
    elo int not null default 1500
    );

Create Table game(
    id int primary key auto_increment,
    player1 varchar(32),
    player2 varchar(32),
    foreign key (player1) references player(username) on update cascade on delete cascade,
    foreign key (player2) references player(username) on update cascade on delete cascade
    );

Create Table participant(
    player varchar(32),
    game int,
    score int,
    primary key (player, game),
    foreign key (player) references player(username) on update cascade on delete cascade,
    foreign key (game) references game(id) on update cascade on delete cascade
    );

-- Everytime a disk is placed in a game, it is recorded in this table
Create Table disk(
    x_pos int,
    y_pos int,
    primary key (x_pos, y_pos),
    player varchar(32),
    game int,
    foreign key (game) references game(id) on update cascade on delete cascade,
    foreign key (player) references player(username) on update cascade on delete cascade
    );

-- Command for leaderboard
Select username, elo from player order by elo desc limit 10;
-- Command for creating player account
insert into player (username, password, elo) values (usernameInput, passwordInput, 1500);
-- command for deleting user, we need to ask the deleting user to verify their username and password
Delete from player where username = usernameInput and password = passwordinput;
-- command for adding activegames instance
Insert into game (player1, player2) values (player1id, player2id);
-- command updating ActiveGame state when player makes move
-- insert into disk (

-- Command for deleting game once it is finished
Delete from game where id = currentgame;
-- figure out online server

-- Command for updating leaderboard values
Update player Set elo = 1130 Where username = 'user4';
Update player Set elo = 1530 Where username = '';
Update player Set username = 'roi', password = 'roi' Where username = '';


insert into player (username, password, elo) values ('user1', 'pass1', 1500);