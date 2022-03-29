# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley

from game.location.location import Location

class Player:
    
    def __init__(self, x, y):
        self._location = Location(x, y)
        self.velocity = (1,0)
        self._symbol = "@"
        self._text_size = 45
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
        self.velocity = value
        self._location.move(self.velocity[0], self.velocity[1])
    
    def get_velocity(self):
        return self.velocity

    def set_velocity(self,velocity):
        self.velocity = velocity

    def set_color(self,color):
        self._color = color