# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley

from game.location.location import Location

class Player:
    
    def __init__(self, x, y):
        self._location = Location(x, y)
        self._symbol = "#"
        self._text_size = 50
        self._color = (0,255,255)
        

    def get_x(self):
        return self._location.get_x()

    def get_y(self):
        return self._location.get_y()

    def get_symbol(self):
        return self._symbol

    def get_text_size(self):
        return self._text_size

    def get_color(self):
        return self._color

    def move_x(self, value):
<<<<<<< HEAD
        self._location.move(value.get_x(),value.get_y())
=======
        self._location.move(value.get_x(),0)
        self._location.move(value.get_x(),0)
<<<<<<< Updated upstream
        self._location.move(value.get_x(),0)
=======
>>>>>>> db95c893903407f9893e73a5d9d89aa1d0a28e75
>>>>>>> Stashed changes
