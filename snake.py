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
class Cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        distance = self.w // self.rows
        # i = row, j = column
        i = self.pos[0]
        j = self.pos[1]

        # Make the cube slightly smaller than the square it is being drawn on so it doesn't cover the grid lines
        pygame.draw.rect(surface, self.color, (i * distance + 1,  j * distance + 1,  distance - 2, distance - 2))

        # Draw the snakes eyes to distingquish the head
        if eyes:
            center = distance // 2
            radius = 3
            circleMiddle = (i * distance + center - radius, j * distance + 8)
            circleMiddle2 = (i * distance + distance - radius * 2, j * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


# Class structure for snake to move around and grow if it eats the food
class Snake(object):
    body = []
    turns = {}

    def __init__(self, color,pos):
        self.color = color
        self.head = Cube(pos)
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

            for index, cube in enumerate(self.body):
                position = cube.pos[:]
                if position in self.turns:
                    turn = self.turns[position]
                    cube.move(turn[0], turn[1])
                    if index == len(self.body) - 1:
                        self.turns.pop(position)
                # Check if the snake goes out of bounds
                else:
                    # If snake reaches the left side of the screen move it to the right side
                    if cube.dirnx == -1 and cube.pos[0] <= 0: cube.pos = (cube.rows-1, cube.pos[1])
                    # If snake reaches the right side of the screen move it to the left side of the screen
                    elif cube.dirnx == 1 and cube.pos[0] >= cube.rows-1: cube.pos = (0, cube.pos[1])
                    # If snake reaches the top of the screen move it to the bottom row
                    elif cube.dirny == 1 and cube.pos[1] >= cube.rows-1: cube.pos = (cube.pos[0], 0)
                    # If snake reaches the bottom of the screen move it to the top row
                    elif cube.dirny == -1 and cube.pos[1] <= 0: cube.pos = (cube.pos[0], cube.rows-1)
                    else: cube.move(cube.dirnx, cube.dirny)


    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)


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
    global rows, width, s
    surface.fill((0, 0, 0))
    s.draw(surface)

    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass

# Message box that pops up after you fail or if you win.
def message_box(subject, content):
    pass


def main():
    global width, rows, s
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))

    # Create snek and set the color to red set it in the middle of the board
    s = Snake((255, 0, 0), (10, 10))

    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        redrawWindow(win)


main()
