import random
from typing import Optional

from room import RoomType


def select_random_room(rooms: int, taken: list[int]) -> int:
    while True:
        room = random.randrange(rooms)
        if room not in taken:
            return room


def get_room_type(room_id: int, rooms: int, boss_room: Optional[int],
                  shop_room: Optional[int]) -> RoomType:
    if room_id == 0:
        return RoomType.ENTRY
    if room_id == rooms - 1:
        return RoomType.EXIT
    if room_id == boss_room:
        return RoomType.BOSS
    if room_id == shop_room:
        return RoomType.SHOP
    return RoomType.BASIC


def get_random_room_location(last_room_location: Point) -> Point:
    return random.choice((
        last_room_location.up,
        last_room_location.down,
        last_room_location.left,
        last_room_location.right,
    ))(1)

