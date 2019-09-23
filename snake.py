# Author: Stephen Farrell
# Date Created: 9/22/2019
# Project: Snake in Python
# Last updated: 9/22/2019


import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Class to create a cube, used to make the snake
class cube(object):
    rows = 0
    w = 0

    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


# Class structure for snake to move around and grow if it eats the food
class snake(object):
    body = []
    turns = {}

    def __init__(self, color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1


    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            for index, cub in enumerate(self.body):
                position = cub.pos[:]
                if position in self.turns:
                    turn = self.turns[position]
                    cub.move(turn[0], turn[1])
                    if index == len(self.body) - 1:
                        self.turns.pop(position)
                # Check if the snake goes out of bounds
                else:
                    # If snake reaches the left side of the screen move it to the right side
                    if cub.dirnx == -1 and cub.pos[0] <= 0: cub.pos = (cub.rows-1, cub.pos[1])
                    # If snake reaches the right side of the screen move it to the left side of the screen
                    elif cub.dirnx == 1 and cub.pos[0] >= cub.rows-1: cub.pos = (0, cub.pos[1])
                    # If snake reaches the top of the screen move it to the bottom row
                    elif cub.dirny == 1 and cub.pos[1] >= cub.rows-1: cub.pos = (cub.pos[0], 0)
                    # If snake reaches the bottom of the screen move it to the top row
                    elif cub.dirny == -1 and cub.pos[1] <= 0: cub.pos = (cub.pos[0], cub.rows-1)
                    else: cub.move(cub.dirnx, cub.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


# Function that draws the grid
def drawGrid(w, rows, surface):
    sizeBetween = w // rows
    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))



def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass

# Message box that pops up after you fail or if you win.
def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))

    # Create snek and set the color to red set it in the middle of the board
    snek = snake((255,0,0), (10, 10))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)

        redrawWindow(win)


main()
