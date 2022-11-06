import sys

from ClassesDefinition import *
MaxPlayerNum = 12
playerlist = []
playercnt = 0

print("РУССКОЕ ЛОТО".center(36,"*"))
print("\n")

lotobag = LotoBag()
inputname = "none"

#add players to the list
print("Зерегистрируйте мгроков (оставьте имя пустым, если больше нет игроков): \n")
while True:
    inputname = input("Имя Игрока №" + str(playercnt+1) + ":")
    if len(inputname) == 0:
        break
    else:
        inpstr = input("Игрок №" + str(playercnt + 1) + " - человек (y/n)?")
        is_human = bool(inpstr == 'y' or inpstr == 'Y')

    playerlist.append(LotoPlayer(inputname, is_human))
    playercnt +=1
    #print(playerlist[len(playerlist)-1].lotocard, playerlist[len(playerlist)-1].name)
    playerlist[len(playerlist)-1].lotocard.lotocardprn()
    if len(playerlist) >= MaxPlayerNum:
        break
#not enough of players
if len(playerlist) <= 1:
    print("\nНедостаточно игроков - завершение программы...")
    sys.exit(-1)
print("\nИгроки введены, начинаем игру!")

nextball = 99
while nextball:
    nextball = lotobag.nextball()
    print("\n")
    print(f'выпало число {nextball:3d}')
    for player in playerlist:
        if not player.active:
            continue
        result = player.checkball(nextball)
        if result == -1:
            print("Игрок " + player.name + " ошибся и выбывает из игры!")
            if len([playerlist[i] for i in range(len(playerlist)) if playerlist[i].active]) <= 1:
                print("\nВ игре осталось недостаточно игроков...")
                nextball=0
                break
        elif result == 1:
            print("Игрок " + player.name + " заполнил все цифры в карточке и победил!")
            nextball=0
            break
        player.lotocard.lotocardprn()

print("Игра завершена. До новых встреч!")