import components
import pygame
import collections
import types

win_width = 550
win_height = 720

window = pygame.display.set_mode((win_width , win_height))

ground = components.Ground(win_width)

pipes : list[components.Pipes] = []
