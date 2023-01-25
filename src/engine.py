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

from player import Player
from utils import get_sound, get_sprite, print_text


class Engine:
    """Class docstring"""

    GAME_STATE = {"START": 1, "RUN": 2, "END": 3, "HIGHSCORE": 4}

    HIGHSCORE_EVENT = USEREVENT + 1

    STARTING_DIRECTION = K_RIGHT

    def __init__(self, title):
        pygame.init()
        self._canvas = display.set_mode((800, 600))
        self._bg = {
            "image": get_sprite("bg_grass.jpg", (800, 600), False),
            "sound": get_sound("background.wav"),
        }
        self._clock = pygame.time.Clock()
        self._state = self.GAME_STATE["START"]
        pygame.display.set_caption(title)

        self.direction_key = self.STARTING_DIRECTION
        self.is_highscore = False
        self.player = Player()

    def mainloop(self):
        """Min loop"""
        self._bg["sound"].play(-1)

        while True:
            self.input()
            self.update()
            self.draw()

    def _init(self):
        self.direction_key = self.STARTING_DIRECTION
        self.is_highscore = False
        self.player.init()

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
            self.player.move(self.direction_key)

            if not self.player.is_alive():
                pygame.time.set_timer(self.HIGHSCORE_EVENT, 3000, 1)
                self._state = self.GAME_STATE["END"]

    def draw(self):
        """Game items draw"""
        self._canvas.blit(self._bg["image"], (0, 0))

        if self._state == self.GAME_STATE["START"]:
            message = {"SNAKE": 70, "Press ENTER to start": 50}
            print_text(self._canvas, message)
        else:
            if self._state == self.GAME_STATE["END"]:
                message = {"You died!": 70, "Your score is: 0": 50}
                print_text(self._canvas, message)
            else:
                self.player.draw(self._canvas)

        display.flip()
        self._clock.tick(4)
