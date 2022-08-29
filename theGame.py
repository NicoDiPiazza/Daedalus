import pygame
import dungeonGen

pygame.init
screen = pygame.display.set_mode([1000, 500])
pygame.event.get()
keys = pygame.key.get_pressed()
#variables for visual

roomNum = 15
def keyPresses():
    pygame.event.game()
print("Hi Nathan")
print("Hello Nico")
# dungeon generation

dungeon = dungeonGen.dunGen(roomNum, True, True)
print(dungeon)
while (keys[pygame.K_q] != True):
    pygame.event.get()
    keys = pygame.key.get_pressed()
    screen = pygame.display.set_mode([1000, 500])
    for i in range(roomNum):
        pygame.draw.circle(screen, [255, 0, 0], [dungeon[i][0] * 500/roomNum, dungeon[i][1] * 500/roomNum], 1)
    pygame.display.update()
