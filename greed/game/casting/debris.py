from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import randint

class Debris(Actor):
    """ Objects that drop from the top of the screen. "rocks and gems".

      Attributes:
        _value (int): The number of points the debis object is worth. 
        _text (string): The text to display
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
        _font_size (int): The font size to use.
        _color (Color): The color of the text.

    """
    def __init__(self, value: int, text: str, position: Point, font_size: int = 15, velocity: Point = Point(0, 0)):

        super().__init__()
        self._value = value
        self._text = text
        self._position = position
        self._velocity = velocity
        self._font_size = font_size
        self._color = Color(randint(0,255),randint(0,255),randint(0,255))
    
    def get_value(self):
        """ Returns the points value of the debris object (Used to keep track of the players score.)
        """
        return self._value