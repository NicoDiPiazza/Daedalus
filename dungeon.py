import random
from typing import Union

# variables for generation


def generate(rooms: int, boss: bool, shop: bool) -> list[list[Union[int, str]]]:
    roomsNeeded = 2
    if boss:
        roomsNeeded = roomsNeeded + 1
    if shop:
        roomsNeeded = roomsNeeded + 1

    if rooms < roomsNeeded:
        print("Not enough rooms!")
        return "Not enough rooms!"

    dunArray: list[list[Union[int, str]]] = [[5, 5]]

    # pick a random room number to be the entry room
    entry = random.randrange(rooms - 1)

    # pick a room for the boss, but make sure it's not the entry room
    newBoss = boss
    bossRoom = -1
    while newBoss:
        # bossRoom = floor(random_func() * (N_rooms - 1))
        bossRoom = random.randrange(rooms - 1)
        newBoss = bossRoom == entry

    # pick a room number for the shop, but make sure it's not one of the rooms
    # for boss or entry
    newShop = shop
    shopRoom = -1
    while newShop:
        # shopRoom = floor(random_func() * (N_rooms - 1))
        shopRoom = random.randrange(rooms - 1)
        newShop = shopRoom == entry or shopRoom == bossRoom

    # coordinate generation
    for i in range(rooms - 1):
        redo = True
        while redo:
            direction = random.random() * 4
            if direction <= 1:
                newCoords = [dunArray[i - 1][0] - 1, dunArray[i - 1][1]]
            elif direction <= 2:
                newCoords = [dunArray[i - 1][0] + 1, dunArray[i - 1][1]]
            elif direction <= 3:
                newCoords = [dunArray[i - 1][0], dunArray[i - 1][1] - 1]
            else:
                newCoords = [dunArray[i - 1][0], dunArray[i - 1][1] + 1]
            redo = newCoords in dunArray
        dunArray.append(newCoords)

    for i in range(rooms):
        if i == entry:
            dunArray[i].append("entry")
        elif i == rooms - 1:
            dunArray[i].append("exit")
        elif i == bossRoom and boss:
            dunArray[i].append("boss")
        elif i == shopRoom and shop:
            dunArray[i].append("shop")
        else:
            dunArray[i].append("basic")

    return dunArray
