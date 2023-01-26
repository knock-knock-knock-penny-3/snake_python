""" docstring """

from pygame.font import Font
from pygame.surface import Surface


class Score:
    """docstring"""

    def __init__(self):
        self._font = Font(None, 25)
        self._multiplier = 10
        self._points = 0

    def init(self):
        """docstring"""

        self._points = 0

    def update(self, food):
        """docstring"""

        self._points = food.eated * self._multiplier

    def draw(self, surface):
        """docstring"""

        topleft = (10, 10)

        score = self._font.render(f"SCORE: {self._points}", True, (4, 27, 4))
        bg_score = Surface(score.get_size())
        bg_score.set_alpha(128)
        bg_score.fill((255, 255, 255))

        surface.blit(bg_score, topleft)
        surface.blit(score, topleft)

    @property
    def points(self):
        """docstring"""
        return self._points
