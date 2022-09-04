"""
Этот файл использовался для тестов функций и операций
при разработке.

Игнорируйте этот файл
"""


import random

def num_of_nonzero(srclist): #Function - finds number of non-zero elemnts in number list
   return len([srclist[i] for i in range(len(srclist)) if srclist[i] > 0])

def cardprint(numlist, allnums, title):
   print(title.center(36, '='))
   for row in range(len(numlist)):
      for col in range(len(numlist[row])):
         if numlist[row][col] == 0:
            print('    ', end='')
         else:
            print(' -- ' if (numlist[row][col] in allnums) else f' {numlist[row][col]:2d} ', end='')
      print('')
   print('='*36)
#create one loto card as a list
MaxRows=3
MaxCol=9
numbers = [0] * MaxRows
for i in range(MaxRows):
   numbers[i]=[0]*MaxCol


#get list of all numbers for loto
allnums = [num for num in range(1,91)]

#prepare one loto card - test of random picking from number list
for i in range(15):
   rndint = random.randint(1, 90)
   while  allnums[rndint-1] <= 0:
      rndint = random.randint(1, 90)
   allnums[rndint-1] = 0
   print(rndint)


   # calc best column
   free_col = -1
   bestcol = (rndint - 1) // 10
   print(f'bestcol {bestcol}')

   for shiftcol in range(MaxCol):
      nextcol = bestcol + shiftcol if (bestcol + shiftcol) < MaxCol else bestcol
      prevcol = bestcol - shiftcol if (bestcol - shiftcol) > 0 else bestcol
      print(f'nextcol {nextcol}; prevcol {prevcol}')
      # find best row - where minimum fields has been filled
      bestrow = 0
      num_of_nz = 5
      for i in range(MaxRows):
         if num_of_nonzero(numbers[i]) < num_of_nz and numbers[i][nextcol] == 0:
            num_of_nz = num_of_nonzero(numbers[i])
            bestrow = i
            free_col = nextcol
      if free_col < 0:
         bestrow = 0
         num_of_nz = 5
         for i in range(MaxRows):
            if num_of_nonzero(numbers[i]) < num_of_nz and numbers[i][prevcol] == 0:
               num_of_nz = num_of_nonzero(numbers[i])
               bestrow = i
               free_col = prevcol
      print(f'bestrow {bestrow}')
      if free_col >= 0:
         print(f'freecol {free_col}')
         break
      #worst case - no suitable place found

   numbers[bestrow][free_col] = rndint





cardprint(numbers, allnums, 'Player1')

print(allnums)
print(num_of_nonzero(allnums))

