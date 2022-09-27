import pprint

import pygame
import dungeons


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode([800, 800])

    # print("Hi Nathan")
    # print("Hello Nico")

    dungeon = dungeons.generate(rooms=16, boss=True, shop=True)

    for i, room in enumerate(dungeon):
        print(f"Room {i}: \t\t{room}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the circles
        for room in dungeon:
            room.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
