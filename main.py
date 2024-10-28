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