import pygame
import dungeon

pygame.init()
screen = pygame.display.set_mode([1000, 500])
pygame.event.get()
keys = pygame.key.get_pressed()
# variables for visual

roomNum = 15


print("Hi Nathan")
print("Hello Nico")
# dungeon generation

# Current --v
# dungeon: list[list[Union[int, str]]]
# Want --v
# dungeon: list[tuple[int, int, str]] OR list[Room]
d = dungeon.generate(roomNum, True, True)
print(d)

while keys[pygame.K_q] != True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    screen = pygame.display.set_mode([1000, 500])
    for i in range(roomNum):
        pygame.draw.circle(
            screen,
            [255, 0, 0],
            [d[i][0] * 500 / roomNum, d[i][1] * 500 / roomNum],
            5,
        )
    pygame.display.update()
