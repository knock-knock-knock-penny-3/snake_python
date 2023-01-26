"""docstring"""

from collections import deque

from pygame.display import get_window_size
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.sprite import Sprite

from utils import get_sound, get_sprite


class Player(Sprite):
    """docstring"""

    DIR = {K_UP: (0, -1), K_DOWN: (0, 1), K_LEFT: (-1, 0), K_RIGHT: (1, 0)}

    INITIAL_POS = (7, 5)

    def __init__(self):
        super().__init__()
        self._alive = True
        self._dead_sound = get_sound("dead.wav")
        self._move_sound = get_sound("slither.wav")
        self._position = self.INITIAL_POS
        self._size = (50, 50)
        self._sprite = get_sprite("player.png", self._size)
        self._snake = deque()

    def init(self):
        """docstring"""
        self._alive = True
        self._move_sound.play(-1)
        self._position = self.INITIAL_POS
        self._snake.clear()
        self._snake.append(self._position)

    def move(self, keydown, food):
        """docstring"""
        if self._alive:
            pos_x, pos_y = self._position
            dir_x, dir_y = self.DIR[keydown]

        self._position = (pos_x + dir_x, pos_y + dir_y)

        self._update(food)

    def _update(self, food):
        win_w, win_h = get_window_size()

        # snake eat food
        # to implement

        # snake eat food
        if self._position == food.position:
            food.eaten()
        # snake eat itself
        elif self._snake.count(self._position):
            self.die()
        elif (
            self._position[0] < 0
            or self._position[0] >= win_w / self._size[0]
            or self._position[1] < 0
            or self._position[1] >= win_h / self._size[1]
        ):
            self.die()
        else:
            self._snake.pop()

        self._snake.appendleft(self._position)

    def draw(self, canvas):
        """docstring"""
        for piece_coords in self._snake:
            pos_x, pos_y = piece_coords
            size_w, size_h = self._size
            canvas.blit(self._sprite, (pos_x * size_w, pos_y * size_h))

    def die(self):
        """docstring"""
        self._alive = False
        self._move_sound.stop()
        self._dead_sound.play()

    @property
    def snake(self):
        """docstring"""
        return self._snake

    def is_alive(self):
        """docstring"""
        return self._alive
