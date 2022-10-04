from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __mul__(self, factor: int) -> "Point":
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def as_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def up(self, amount: int) -> "Point":
        return Point(self.x, self.y - amount)

    def down(self, amount: int) -> "Point":
        return Point(self.x, self.y + amount)

    def left(self, amount: int) -> "Point":
        return Point(self.x - amount, self.y)

    def right(self, amount: int) -> "Point":
        return Point(self.x + amount, self.y)
