import random

MaxNumInLotoCard = 15
MaxRows = 3
MaxCol = 9


# Function - finds number of non-zero elemnts in number list
def num_of_nonzero(srclist):
   return len([srclist[i] for i in range(len(srclist)) if srclist[i] > 0])

"""
Описание класса КАРТОЧКА (3х9 клеток, по 5 цифр в строку)
по столбцам 1-10, 11-20, 21-30, ...
"""
class LotoCard:
    #init card with random figures
    def fillcard(self):
        for i in range(15):
            rndint = random.randint(1, 90)
            while self.exist(rndint): #check if number is already in this card
                rndint = random.randint(1, 90)
            # calc best column
            free_col = -1
            bestcol = (rndint - 1) // 10 # best coulumn for new number

            for shiftcol in range(MaxCol):
                nextcol = bestcol + shiftcol if (bestcol + shiftcol) < MaxCol else bestcol
                prevcol = bestcol - shiftcol if (bestcol - shiftcol) > 0 else bestcol
                # find best row - where minimum fields has been filled
                bestrow = 0
                num_of_nz = 5
                for i in range(MaxRows):
                    if num_of_nonzero(self.numbers[i]) < num_of_nz and self.numbers[i][nextcol] == 0:
                        num_of_nz = num_of_nonzero(self.numbers[i])
                        bestrow = i
                        free_col = nextcol
                if free_col < 0:
                    bestrow = 0
                    num_of_nz = 5
                    for i in range(MaxRows):
                        if num_of_nonzero(self.numbers[i]) < num_of_nz and self.numbers[i][prevcol] == 0:
                            num_of_nz = num_of_nonzero(self.numbers[i])
                            bestrow = i
                            free_col = prevcol
                #print(f'bestrow {bestrow}')
                if free_col >= 0:
                    #print(f'freecol {free_col}')
                    break
                # worst case - no suitable place found
            self.numbers[bestrow][free_col] = rndint

    #init
    def __init__(self, ownername):
        self.numbers = [0] * MaxRows
        for i in range(MaxRows):
            self.numbers[i] = [0] * MaxCol
        self.fillcard()
        self.ownername = ownername
        self.bingoballs = []

    def exist(self, number):
        result = False
        for i in range(len(self.numbers)):
            result = result or (number in self.numbers[i])
        return result

    def crossout(self, number):
        if self.exist(number):
            self.bingoballs.append(number)
            return 1 if len(self.bingoballs) >= MaxNumInLotoCard else 0
        else:
            return 0

    def lotocardprn(self):
         print(self.ownername.center(36, '='))
         for row in range(len(self.numbers)):
            for col in range(len(self.numbers[row])):
                if self.numbers[row][col] == 0:
                    print('    ', end='')
                else:
                    print(' -- ' if (self.numbers[row][col] in self.bingoballs) else f' {self.numbers[row][col]:2d} ', end='')
            print('')
         print('=' * 36)
"""
Описание класса МЕШОК (1..90)
"""
class LotoBag:

    def __init__(self):
        self.balls = [num for num in range(1,91)]
        self.selected = []

    def nextball(self):
        if not self.balls:
            return 0
        newball = self.balls[random.randint(0, len(self.balls)-1)]
        self.balls.remove(newball)
        self.selected.append(newball)
        return newball

"""
Описание класса ИГРОК
"""
class LotoPlayer:

    def __init__(self, title, is_human):
        self.name = title
        self.human = is_human
        self.active = True
        self.lotocard = LotoCard(self.name)

    def checkball(self, ball):
        if self.human:
            choice = input("Игрок " + self.name + ", вычеркиваем число (y/n)? ")
            num_exists = self.lotocard.exist(ball)
            if (num_exists and (choice == 'n' or choice == 'N')) or (not num_exists and (choice == 'y' or choice == 'Y')):
                self.active = False
                #print("Checkball: Игрок " + self.name + " ошибся и выбывает из игры!")
                return -1
        return self.lotocard.crossout(ball)

