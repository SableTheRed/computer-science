import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



arrowkeys = [K_UP, K_DOWN, K_LEFT, K_RIGHT]
dirvect = []

pygame.init()


screen = pygame.display.set_mode([0,0])

running = True

while running:


    for event in pygame.event.get():
            if event.type == KEYDOWN:
                 
                if event.key == K_ESCAPE:
                    running = False

                if event.key in arrowkeys:
                     pass


            elif event.type == QUIT:
                running = False
    screen.fill((200, 210, 200))
    pygame.display.flip()

