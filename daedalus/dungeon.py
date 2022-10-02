import random
from typing import Iterator

from daedalus.dungeons import (DungeonRoom, Point, get_random_room_location,
                               get_room_type, select_random_room)


def fill_random_room(rooms: int, taken: list[int]) -> int:
    while True:
        room = random.randrange(rooms)
        if room not in taken:
            taken.append(room)
            return room


class Dungeon:

    def __init__(self, rooms: int, boss: bool, shop: bool) -> None:
        rooms_needed = 2 + int(boss) + int(shop)
        if rooms < rooms_needed:
            raise ValueError("not enough rooms")

        taken = [0, rooms - 1]
        self.rooms: list[DungeonRoom] = []

        boss_room = fill_random_room(rooms, taken)
        shop_room = fill_random_room(rooms, taken)

        for i in range(rooms):
            self.rooms.append(
                DungeonRoom(self.get_next_room_location(i, Point(7, 7)),
                            get_room_type(i, rooms, boss_room, shop_room)))

    def __iter__(self) -> Iterator[DungeonRoom]:
        return iter(self.rooms)

    def is_room_taken(self, next: Point) -> bool:
        for room in self.rooms:
            if room.location.x == next.x and room.location.y == next.y:
                return True
        return False

    def get_next_room_location(self, identifier: int, start: Point) -> Point:
        if identifier < 0:
            raise ValueError(
                f"expected identifier larger than 0, got {identifier}")
        if identifier == 0:
            return start
        last_room_location = self.rooms[identifier - 1].location
        while True:
            next = get_random_room_location(last_room_location)
            if not self.is_room_taken(next):
                return next
