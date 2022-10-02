from dataclasses import dataclass
from enum import Enum, auto

import pygame
from pygame.surface import Surface

from dmath import Point


class RoomType(Enum):
    BASIC = auto()
    BOSS = auto()
    ENTRY = auto()
    EXIT = auto()
    SHOP = auto()


ROOM_COLORS: dict[RoomType, tuple[int, int, int]] = {
    RoomType.BASIC: (0, 0, 255),
    RoomType.BOSS: (255, 0, 0),
    RoomType.ENTRY: (255, 255, 0),
    RoomType.EXIT: (255, 255, 0),
    RoomType.SHOP: (0, 255, 0),
}


@dataclass
class DungeonRoom:
    location: Point
    type: RoomType

    def __str__(self) -> str:
        return f"{self.type}: {self.location}"

    def draw(self, surface: Surface) -> None:
        pygame.draw.circle(
            surface,
            ROOM_COLORS[self.type],
            # (self.location.x * 20, self.location.y * 20),
            (self.location * 20).as_tuple(),
            5,
        )
