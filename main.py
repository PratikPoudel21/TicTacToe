import pygame
import os
from pygame.locals import *

pygame.init() 

WIDTH = HEIGHT = 600 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Tic-Tac-Toe") 

# console board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

screen.fill((255, 255, 255)) 

#  vertical lines
pygame.draw.line(screen, (0, 0, 0), (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 4) # first 
pygame.draw.line(screen, (0, 0, 0), (WIDTH - WIDTH / 3, 0), (WIDTH - WIDTH / 3, HEIGHT), 4) # second

# horizontal lines
pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 4) # first
pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT - HEIGHT / 3), (WIDTH, HEIGHT - HEIGHT / 3), 4) # second

def restart():
    screen.fill((255, 255, 255))
    #  vertical lines
    pygame.draw.line(screen, (0, 0, 0), (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 4) # first 
    pygame.draw.line(screen, (0, 0, 0), (WIDTH - WIDTH / 3, 0), (WIDTH - WIDTH / 3, HEIGHT), 4) # second

    # horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 4) # first
    pygame.draw.line(screen, (0, 0, 0), (0, HEIGHT - HEIGHT / 3), (WIDTH, HEIGHT - HEIGHT / 3), 4) # second
    os.system("cls")

def draw_text(text, text_col,font_size, x, y):
    font = pygame.font.SysFont( "Arial", font_size )
    img = font.render(text, True, text_col)
    rect = img.get_rect()
    rect.center = (x, y)
    screen.blit(img, rect)

def gameOver(winner):
    screen.fill((255, 255, 255))
    draw_text("Game Over!", (0, 0, 0), 100, WIDTH / 2, HEIGHT / 3)
    draw_text(f'"{winner}" wins the game', (0, 0, 0), 50, WIDTH / 2, HEIGHT / 2)
    draw_text('Press "R" to restart', (0, 0, 0), 30, WIDTH / 2, HEIGHT / 2 + 50)
    draw_text('Press "Esc" to exit', (0, 0, 0), 30, WIDTH / 2, HEIGHT / 2 + 90)
 
def mark(x, y, turn):
    gameover = False
    min = WIDTH if WIDTH < HEIGHT else HEIGHT

    if x <= WIDTH / 3 and y <= HEIGHT / 3: # first square
        if board[0][0] == 0:
            draw_text(turn, (0, 0, 0), int(min/3),  WIDTH / 6, HEIGHT / 6)
            board[0][0] = turn
            if(board[1][0] == board[2][0] == turn) or (board[0][1] == board[0][2] == turn) or (board[1][1] == board[2][2] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x > WIDTH / 3 and x <= WIDTH - WIDTH / 3 and y <= HEIGHT / 3: # second square
        if board[0][1] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH / 2, HEIGHT / 6)
            board[0][1] = turn
            if (board[0][0] == board[0][2] == turn) or (board[1][1] == board[2][1] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x > WIDTH - WIDTH / 3 and x <= WIDTH and y <= HEIGHT / 3: # third square
        if board[0][2] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH - WIDTH / 6, HEIGHT / 6)
            board[0][2] = turn
            if (board[0][0] == board[0][1] == turn) or (board[1][1] == board[2][0] == turn) or (board[1][2] == board[2][2] == turn): 
                gameover = True
                gameOver(turn)
            turn =  "O" if turn == "X" else "X"

    elif x <= WIDTH / 3 and y > HEIGHT / 3 and y <= HEIGHT - HEIGHT / 3: # fourth square
        if board[1][0] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH / 6, HEIGHT / 2)
            board[1][0] = turn
            if (board[0][0] == board[2][0] == turn) or (board[1][1] == board[1][2] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x > WIDTH / 3 and x <= WIDTH - WIDTH / 3 and y > HEIGHT / 3 and y <= HEIGHT - HEIGHT / 3: # fifth square
        if board[1][1] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH / 2, HEIGHT / 2)
            board[1][1] = turn
            if (board[0][0] == board[2][2] == turn) or (board[0][2] == board[2][0] == turn) or (board[0][1] == board[2][1] == turn) or (board[1][0] == board[1][2] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x > WIDTH - WIDTH / 3 and x <= WIDTH and y > HEIGHT / 3 and y <= HEIGHT - HEIGHT / 3: # sixth square
        if board[1][2] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH - WIDTH / 6, HEIGHT / 2)
            board[1][2] = turn
            if (board[0][2] == board[2][2] == turn) or (board[1][1] == board[1][0] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x <= WIDTH / 3 and y > HEIGHT - HEIGHT / 3 and y <= HEIGHT: # seventh square
        if board[2][0] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH / 6, HEIGHT - HEIGHT / 6)
            board[2][0] = turn
            if (board[1][0] == board[0][0] == turn) or (board[1][1] == board[0][2] == turn) or (board[2][1] == board[2][2] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x > WIDTH / 3 and x <= WIDTH - WIDTH / 3 and y > HEIGHT - HEIGHT / 3 and y <= HEIGHT: # eighth square
        if board[2][1] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH / 2, HEIGHT - HEIGHT / 6)
            board[2][1] = turn
            if (board[2][0] == board[2][2] == turn) or (board[1][1] == board[0][1] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"

    elif x > WIDTH - WIDTH / 3 and x <= WIDTH and y > HEIGHT - HEIGHT / 3 and y <= HEIGHT: # nineth square
        if board[2][2] == 0:
            draw_text(turn, (0, 0, 0), int(min/3), WIDTH - WIDTH / 6, HEIGHT - HEIGHT / 6)
            board[2][2] = turn
            if (board[1][2] == board[0][2] == turn) or (board[1][1] == board[0][0] == turn) or (board[2][1] == board[2][0] == turn): 
                gameover = True
                gameOver(turn)
            turn = "O" if turn == "X" else "X"
            
    return (turn, gameover)

turn = "X"
running = True
GAMEOVER = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

            elif event.key == K_r:
                restart()
                board = [
                    [0, 0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0]
                ]
                GAMEOVER = False
                turn = "X"

        elif not GAMEOVER and event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                turn, GAMEOVER = mark(x, y, turn)

                
                print("-------------")
                for i in range(3):
                    for j in range(3):
                        print(f"| {board[i][j]}", end=" ")
                    print("| \n", end="")
                    print("-------------")
                print("\n", end="")

    pygame.display.flip()

pygame.quit()