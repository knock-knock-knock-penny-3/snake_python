""" Module docstring """

import sys
import pygame
from pygame import display
from pygame.constants import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
    QUIT,
    USEREVENT,
)

from utils import get_sound, get_sprite


class Engine:
    """Class docstring"""

    GAME_STATE = {"START": 1, "RUN": 2, "END": 3, "HIGHSCORE": 4}

    HIGHSCORE_EVENT = USEREVENT + 1

    STARTING_DIRECTION = K_RIGHT

    def __init__(self, title):
        pygame.init()
        self._canvas = display.set_mode((800, 600))
        self._bg_image = get_sprite("bg_grass.jpg", (800, 600), False)
        self._bg_sound = get_sound("background.wav")
        self._clock = pygame.time.Clock()
        self._state = self.GAME_STATE["START"]
        pygame.display.set_caption(title)

        self.direction_key = self.STARTING_DIRECTION
        self.is_highscore = False

    def mainloop(self):
        """Min loop"""
        self._bg_sound.play(-1)

        while True:
            self.input()
            self.update()
            self.draw()

    def _init(self):
        self.direction_key = self.STARTING_DIRECTION
        self.is_highscore = False

    def input(self):
        """User input management"""
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == self.HIGHSCORE_EVENT:
                self._state = self.GAME_STATE["HIGHSCORE"]

            if event.type == KEYDOWN:
                if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    self.direction_key = event.key
                elif event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_RETURN and self._state in [
                    self.GAME_STATE["START"],
                    self.GAME_STATE["HIGHSCORE"],
                ]:
                    self._init()
                    self._state = self.GAME_STATE["RUN"]

    def update(self):
        """Game data update"""
        if self._state == self.GAME_STATE["RUN"]:
            pass

    def draw(self):
        """Game items draw"""
        self._canvas.blit(self._bg_image, (0, 0))

        display.flip()
        self._clock.tick(4)
