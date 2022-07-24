import random

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
        self.history = []

    def add(self, count):
        """
        Добавить деньги на счет
        :param count:
        :return:
        """
        self.money += count


"""
Описание класса МЕШОК (1..90)
"""
class LotoBag:
    pass
    def __init__(self):
        self.money = 0
        self.history = []

    def add(self, count):
        """
        Добавить деньги на счет
        :param count:
        :return:
        """
        self.money += count

"""
Описание класса ИГРОК
"""
class LotoPlayer:
    pass
    def __init__(self):
        self.money = 0
        self.history = []

    def add(self, count):
        """
        Добавить деньги на счет
        :param count:
        :return:
        """
        self.money += count