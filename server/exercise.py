class Exercise:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

        def __str__(self):
            return f'{self.num1} {self.op} {self.num2}'