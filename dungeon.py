import random
from typing import Union


def generate(rooms: int, boss: bool, shop: bool) -> list[list[Union[int, str]]]:
    # The dungeon needs to contain at least two rooms, one of which being the
    # entrance. If shop is true, we add one room for the shop, and if boss is
    # true, we add another for the shop.
    rooms_needed = 2
    if boss:
        rooms_needed += 1
    if shop:
        rooms_needed += 1

    # If the amount of rooms that we 'request' is smaller than the amount of
    # required rooms, raise a ValueError
    if rooms < rooms_needed:
        raise ValueError("Not enough rooms!")

    # This list represents the dungeon as a whole. This is what will be later
    # returned.
    dun_array: list[list[Union[int, str]]] = [[5, 5]]

    # pick a random room number to be the entry room
    entry = random.randrange(rooms - 1)

    # pick a room for the boss, but make sure it's not the entry room
    new_boss = boss
    boss_room = -1
    while new_boss:
        boss_room = random.randrange(rooms - 1)
        new_boss = boss_room == entry

    # pick a room number for the shop, but make sure it's not one of the rooms
    # for boss or entry
    new_shop = shop
    shop_room = -1
    while new_shop:
        shop_room = random.randrange(rooms - 1)
        new_shop = shop_room == entry or shop_room == boss_room

    # We generate the rooms in a snake pattern. We start at the original room,
    # then we choose a random direction in which to go from there. Then we just
    # keep doing that until we're out of rooms. The redo flag here is in case we
    # land on a room that already exists. If that happens we just pick a
    # different direction to go.
    for i in range(rooms - 1):
        redo = True
        while redo:
            direction = random.random() * 4
            if direction <= 1:
                new_coords = [dun_array[i - 1][0] - 1, dun_array[i - 1][1]]
            elif direction <= 2:
                new_coords = [dun_array[i - 1][0] + 1, dun_array[i - 1][1]]
            elif direction <= 3:
                new_coords = [dun_array[i - 1][0], dun_array[i - 1][1] - 1]
            else:
                new_coords = [dun_array[i - 1][0], dun_array[i - 1][1] + 1]
            redo = new_coords in dun_array
        dun_array.append(new_coords)

    # Go through all of the rooms. If the current number matches the number
    # assigned to the boss or shop room, add it to the corresponding room list.
    # If it's the final room, mark it as the exit room. The entry room is a
    # random room selected at the beginning. All of the remaining rooms are
    # marked as basic.
    for i in range(rooms):
        if i == entry:
            dun_array[i].append("entry")
        elif i == rooms - 1:
            dun_array[i].append("exit")
        elif i == boss_room and boss:
            dun_array[i].append("boss")
        elif i == shop_room and shop:
            dun_array[i].append("shop")
        else:
            dun_array[i].append("basic")

    # Finally, we return the list that represents the dungeon.
    return dun_array
