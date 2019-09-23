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

    def move(self):
        pass

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
