"""docstring"""

import pickle
from pygame.math import Vector2

from utils import get_font, get_path


class HighScore:
    """docstring"""

    def __init__(self):
        self._filepath = get_path("assets/data/highscores.bin")
        self._highscores = self.load()
        self._new_name = []
        self._text_color = (4, 27, 4)

    def load(self):
        """docstring"""
        try:
            with open(self._filepath, "rb") as highscore_file:
                return pickle.load(highscore_file)
        except FileNotFoundError:
            return {}

    def save(self):
        """docstring"""
        with open(self._filepath, "wb") as highscore_file:
            pickle.dump(self._highscores, highscore_file)

    def check(self, points):
        """docstring"""
        for score in self._highscores:
            if points > score[1]:
                return True

        return False

    def add_name(self, canvas, points):
        """docstring"""
        base_top = 200

        title = self._draw_text(canvas, (0, base_top), 70, "Enter your name:")

        char_size = 100
        for i, char in enumerate(self._new_name):
            self._draw_text(
                canvas,
                ((char_size * (i - 1)) - char_size / 2, base_top + title["size"] + 20),
                char_size,
                char,
            )

        if len(self._new_name) == 3:
            self._highscores.append(("".join(self._new_name).upper(), points))
            self._highscores = sorted(
                self._highscores, key=lambda player: player[1], reverse=True
            )
            self._highscores.pop()
            self.save()
            self._new_name = []
            return True

        return False

    def add_char(self, char):
        """docstring"""
        if 48 <= char <= 57 or 97 <= char <= 122:
            self._new_name.append(chr(char))

    def print(self, canvas):
        """docstring"""
        base_top = 100

        title = self._draw_text(canvas, (0, base_top), 70, "HIGH SCORE")
        label = {"gap": 0, "size": 40, "width": 200}
        label["top"] = base_top + title["size"] + label["gap"]

        for name_text, score_text in self._highscores:
            self._draw_text(
                canvas, (-(label["width"] / 2), label["top"]), label["size"], name_text
            )

            self._draw_text(
                canvas, (label["width"] / 2, label["top"]), label["size"], score_text
            )

            label["top"] += label["size"] + label["gap"]

    def _draw_text(self, canvas, base, font_size, text_str):
        base_left, base_top = base

        text = {"size": font_size}
        text["obj"] = get_font("golden_age.ttf", text["size"])
        text["surface"] = text["obj"].render(str(text_str), True, self._text_color)
        text["rect"] = text["surface"].get_rect()
        text["rect"].center = Vector2(canvas.get_width() / 2 + base_left, base_top)
        canvas.blit(text["surface"], text["rect"])

        return text
