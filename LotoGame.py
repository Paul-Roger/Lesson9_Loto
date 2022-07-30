import sys

from ClassesDefinition import *
MaxPlayerNum = 12
playerlist = []
playercnt = 0

print("РУССКОЕ ЛОТО".center(36,"*"))
print("\n")
inputname = "none"

#add players
while len(inputname) > 0:
    print("Зерегистрируйте мгроков (оставьте имя пустым, если больше нет игроков): \n")
    inputname = input("Имя Игрока №" + str(playercnt+1) + ":")
    if inputname:
        inpstr = input("Игрок №" + str(playercnt + 1) + " - человек (y/n)?")
        is_human = (inpstr == 'y' or inpstr == 'Y')
    playerlist.append(LotoPlayer(is_human))
    print(playerlist[len(playerlist)].lotocard, playerlist[len(playerlist)].name)
    if len(playerlist) >= MaxPlayerNum:
        break
#not enough of players
if len(playerlist) <= 1:
    print("Недостаточно игроков - завершение программы...")
    sys.exit(-1)

print("Игроки введены, начинаем игру!")


