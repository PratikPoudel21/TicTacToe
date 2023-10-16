import pygame
from pygame.locals import *

pygame.init()

WIDTH = HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

screen.fill((255, 255, 255))
pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 4)
pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 4)
pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 4)
pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 4)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if x <= 200 and y <= 200:
                    print("1")
                elif x > 200 and x <= 400 and y <= 200:
                    print("2")
                elif x > 400 and x <= 600 and y <= 200:
                    print("3")
                elif x <= 200 and y > 200 and y <= 400:
                    print("4")
                elif x > 200 and x <= 400 and y > 200 and y <= 400:
                    print("5")
                elif x > 400 and x <= 600 and y > 200 and y <= 400:
                    print("6")
                elif x <= 200 and y > 400 and y <= 600:
                    print("7")
                elif x > 200 and x <= 400 and y > 400 and y <= 600:
                    print("8")
                elif x > 400 and x <= 600 and y > 400 and y <= 600:
                    print("9")
                
    

    pygame.display.flip()


