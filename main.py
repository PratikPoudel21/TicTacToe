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

text_font = pygame.font.SysFont("Arial", 200)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    rect = img.get_rect()
    rect.center = (x, y)
    screen.blit(img, rect)

running = True
turn = "X"

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
                if x <= 200 and y <= 200: # first square
                    draw_text(turn, text_font, (0, 0, 0), 100, 100)

                elif x > 200 and x <= 400 and y <= 200: # second square
                    draw_text(turn, text_font, (0, 0, 0), 300, 100)

                elif x > 400 and x <= 600 and y <= 200: # third square
                    draw_text(turn, text_font, (0, 0, 0), 500, 100)

                elif x <= 200 and y > 200 and y <= 400: # fourth square
                    draw_text(turn, text_font, (0, 0, 0), 100, 300)

                elif x > 200 and x <= 400 and y > 200 and y <= 400: # fifth square
                    draw_text(turn, text_font, (0, 0, 0), 300, 300)

                elif x > 400 and x <= 600 and y > 200 and y <= 400: # sixth square
                    draw_text(turn, text_font, (0, 0, 0), 500, 300)

                elif x <= 200 and y > 400 and y <= 600: # seventh square
                    draw_text(turn, text_font, (0, 0, 0), 100, 500)

                elif x > 200 and x <= 400 and y > 400 and y <= 600: # eighth square
                    draw_text(turn, text_font, (0, 0, 0), 300, 500)

                elif x > 400 and x <= 600 and y > 400 and y <= 600: # nineth square
                    draw_text(turn, text_font, (0, 0, 0), 500, 500)
                
                turn = "O" if turn == "X" else "X"

    pygame.display.flip()