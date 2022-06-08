from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import randint

class Debris(Actor):
    def __init__(self, value: int = 0, text: str = "", position: Point = Point(0, 0), font_size: int = 15, color: Color = Color(randint(0,255), randint(0,255), randint(0,255)), velocity: Point = Point(0, 0)):

        super().__init__()
        self._value = value
        self._text = text
        self._position = position
        self._velocity = velocity
        self._font_size = font_size
        self._color = color
    
    def get_value(self):
        return self._value