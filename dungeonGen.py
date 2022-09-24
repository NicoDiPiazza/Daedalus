import random
# variables for generation


def dunGen(N_rooms:int, boss:bool, shop:bool):
    from math import floor
    from random import random as random_func

    roomsNeeded = 2
    if boss:
        roomsNeeded = roomsNeeded + 1
    if shop:
        roomsNeeded = roomsNeeded + 1



    if N_rooms < roomsNeeded:
        print("Not enough rooms!")
        return("Not enough rooms!")

    dunArray = []
    startGridCoords = [5, 5]

    # entry = floor(random() * (N_rooms - 1))
    entry = random.randrange(N_rooms - 1)
    newBoss = boss
    bossRoom = -1
    while newBoss:
        # bossRoom = floor(random_func() * (N_rooms - 1))
        bossRoom = random.randrange(N_rooms - 1)
        newBoss = bossRoom == entry
    newShop = shop
    shopRoom = -1
    while newShop:
        # shopRoom = floor(random_func() * (N_rooms - 1))
        shopRoom = random.randrange(N_rooms - 1)
        newShop = shopRoom == entry or shopRoom == bossRoom


# coordinate generation
    for i in range(N_rooms):

        if i > 0:
            redo = True

            while redo:
                direction = random_func() * 4
                if direction <= 1:
                    newCoords = [dunArray[i-1][0] - 1, dunArray[i-1][1]]
                elif direction <= 2:
                    newCoords = [dunArray[i-1][0] + 1, dunArray[i-1][1]]
                elif direction <= 3:
                    newCoords = [dunArray[i-1][0], dunArray[i-1][1] - 1]
                else:
                    newCoords = [dunArray[i-1][0], dunArray[i-1][1] + 1]

                redo = newCoords in dunArray


            dunArray.append(newCoords)
        else:
            dunArray.append(startGridCoords)


    for i in range(N_rooms):

        if i == entry:
            dunArray[i].append('entry')
        elif i == N_rooms - 1:
            dunArray[i].append('exit')
        elif i == bossRoom and boss:
            dunArray[i].append('boss')
        elif i == shopRoom and shop:
            dunArray[i].append('shop')

        else:
            dunArray[i].append('basic')

    return dunArray
