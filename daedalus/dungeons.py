import random
from dataclasses import dataclass
from typing import Optional

import pygame
from pygame.surface import Surface


ROOM_COLORS = {
    "basic": (0, 0, 255),
    "shop": (0, 255, 0),
    "entry": (255, 255, 0),
    "exit": (255, 255, 0),
    "boss": (255, 0, 0),
}


@dataclass
class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def up(self, amount: int) -> "Point":
        return Point(self.x, self.y - amount)

    def down(self, amount: int) -> "Point":
        return Point(self.x, self.y + amount)

    def left(self, amount: int) -> "Point":
        return Point(self.x - amount, self.y)

    def right(self, amount: int) -> "Point":
        return Point(self.x + amount, self.y)


@dataclass
class DungeonRoom:
    location: Point
    type: str

    def __str__(self) -> str:
        return f"{self.location}\t\t{self.type}"

    def draw(self, surface: Surface) -> None:
        pygame.draw.circle(
            surface,
            ROOM_COLORS[self.type],
            (self.location.x * 20, self.location.y * 20),
            5,
        )


def select_random_room(rooms: int, taken: list[int]) -> int:
    while True:
        room = random.randrange(rooms)
        if room not in taken:
            return room


def get_room_type(
    room_id: int, rooms: int, boss_room: Optional[int], shop_room: Optional[int]
) -> str:
    if room_id == 0:
        return "entry"
    if room_id == rooms - 1:
        return "exit"
    if room_id == boss_room:
        return "boss"
    if room_id == shop_room:
        return "shop"
    return "basic"


def is_room_taken(dungeon: list[DungeonRoom], next: Point) -> bool:
    for room in dungeon:
        if room.location.x == next.x and room.location.y == next.y:
            return True
    return False


def get_random_room_location(last_room_location: Point) -> Point:
    return random.choice(
        (
            last_room_location.up,
            last_room_location.down,
            last_room_location.left,
            last_room_location.right,
        )
    )(1)


def get_next_room_location(dungeon: list[DungeonRoom], current: int) -> Point:
    if current < 0:
        raise ValueError(f"expected room id larger than 0, got {current}")
    if current == 0:
        return Point(7, 7)
    last_room_location = dungeon[current - 1].location
    while True:
        next = get_random_room_location(last_room_location)
        if not is_room_taken(dungeon, next):
            return next


def generate(*, rooms: int, boss: bool, shop: bool) -> list[DungeonRoom]:
    # Add one if boss is true, else add 0. Same for shop.
    rooms_needed = 2 + int(boss) + int(shop)
    if rooms < rooms_needed:
        raise ValueError("Not enough rooms!")

    taken = [0, rooms - 1]
    dungeon: list[DungeonRoom] = []

    boss_room = select_random_room(rooms, taken)
    taken.append(boss_room)

    shop_room = select_random_room(rooms, taken)
    taken.append(shop_room)

    for i in range(rooms):
        dungeon.append(
            DungeonRoom(
                get_next_room_location(dungeon, i),
                get_room_type(i, rooms, boss_room, shop_room),
            )
        )

    return dungeon
