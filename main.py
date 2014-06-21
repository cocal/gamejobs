# -*- coding: utf-8 -*-
'''
@author: cocal
'''
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

pygame.display.set_caption("main")

while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    pygame.display.update()