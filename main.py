import sys
import pygame
import numpy as np

pygame.init()

WHITE = (255,255,255)
GREY = (180,180,180)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

WIDTH = HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_ROWS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

screen = pygame.display.set_mode((WIDTH , HEIGHT))

pygame.display.set_caption("Tic Tac Toe")
screen.fill(BLACK)

board = np.zeros((BOARD_ROWS , BOARD_COLS))

def draw_line(color=WHITE):
    for i in range(1 , BOARD_ROWS):
        pygame.draw.line( screen , color , (0 , SQUARE_SIZE*i) , (WIDTH , SQUARE_SIZE*i) , LINE_WIDTH)
        pygame.draw.line( screen , color , (SQUARE_SIZE*i , 0) , (SQUARE_SIZE*i , HEIGHT) , LINE_WIDTH)

def draw_figure(color=WHITE):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]== 1 :
                pygame.draw.circle(screen , color , ( int ( col*SQUARE_SIZE + SQUARE_SIZE // 2 ) )  , (int (row * SQUARE_SIZE + SQUARE_SIZE //2 )),
                                   CIRCLE_RADIUS ,  CIRCLE_WIDTH)
            if board[row][col] ==2:
                pygame.draw.line( screen , color , (col * SQUARE_SIZE // 4 , row * SQUARE_SIZE + SQUARE_SIZE //4) ,
                                  (col*SQUARE_SIZE  + 3 *SQUARE_SIZE //4 , row*SQUARE_SIZE + 3 * SQUARE_SIZE //4)
                                )
                pygame.draw.line( screen , color , (col * SQUARE_SIZE // 4 , row * SQUARE_SIZE + 3*SQUARE_SIZE //4) ,
                                  (col*SQUARE_SIZE  + 3 *SQUARE_SIZE //4 , row*SQUARE_SIZE + SQUARE_SIZE //4)
                                )

def make_square(row , col , player):
    board[row][col] = player

def available_square(row , col ):
    return board[row][col] == 0

def is_board_full(check_board = board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return True
    
    return False

def check_win(player , check_board = board):
    for col in range(BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player :
            return True
        
    for row in range(BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player :
            return True
        
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True 
    
    if check_board[0][2] == player and check_board[1][1] == player and check_board[2][0] == player:
        return True 
    
    return False