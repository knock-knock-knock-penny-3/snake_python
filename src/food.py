""" docstring """

from random import randrange
from pygame.display import get_window_size
from pygame.sprite import Sprite

from utils import get_sound, get_sprite


class Food(Sprite):
    """docstring"""

    def __init__(self, player):
        super().__init__()
        self._chew_sound = get_sound("chew.wav")
        self._eated = 0
        self._player = player
        self._size = (50, 50)
        self._sprite = get_sprite("apple.png", self._size)
        self.position = self._set_random_positions()

    def init(self):
        """docstring"""

        self._eated = 0
        self._spawn()

    def draw(self, canvas):
        """docstring"""

        pos_x, pos_y = self.position
        size_w, size_h = self._size
        canvas.blit(self._sprite, (pos_x * size_w, pos_y * size_h))

    def _set_random_positions(self):
        win_w, win_h = get_window_size()
        return (
            randrange(0, win_w / self._size[0]),
            randrange(0, win_h / self._size[1]),
        )

    def _spawn(self):
        self.position = self._set_random_positions()

        while self._player.snake.count(self.position):
            self.position = self._set_random_positions()

    @property
    def eated(self):
        """docstring"""
        return self._eated

    def eaten(self):
        """docstring"""
        self._chew_sound.play()
        self._eated += 1
        self._spawn()
