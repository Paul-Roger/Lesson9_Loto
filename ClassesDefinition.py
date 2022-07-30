import random

MaxNumInLotoCard = 15

"""
Описание класса КАРТОЧКА (3х9 клеток, по 5 цифр в строку)
по столбцам 1-10, 11-20, 21-30, ...
"""
class LotoCard:

    def __init__(self):
        self.numbers = []
        for i in range(3):
            for j in range(9):
                self.numbers[i][j] = 0
        self.ownername = "none"
        self.bingoballs = []

    def exist(self, number):
        return number in self.numbers

    def crossout(self, number):
        if self.exist(number):
            self.bingoballs.append(number)
            return True if len(self.bingoballs) >= MaxNumInLotoCard else False

"""
Описание класса МЕШОК (1..90)
"""
class LotoBag:

    def __init__(self):
        self.balls = [num for num in range(1,91)]
        self.selected = []

    def nextball(self, ball):
        newball = self.balls[random.randint(0, len(self.balls))]
        self.balls.remove(newball)
        self.selected.append(newball)
        return newball

"""
Описание класса ИГРОК
"""
class LotoPlayer:

    def __init__(self, is_human):
        self.name = ""
        self.human = is_human
        self.active = True
        self.lotocard = LotoCard()

    def checkball(self, ball):
        if self.human:
            choice = input("Игрок " + self.name + ", вычеркиваем число (y/n)? ")
            num_exists = self.lotocard.exist()
            if (num_exists and (choice == 'n' or choice == 'N')) or (not num_exists and (choice == 'y' or choice == 'Y')):
                self.active = False
                # print("Игрок " + self.name + " ошибся и выбывает из игры!")
                return -1
        return self.lotocard.crossout(ball)

