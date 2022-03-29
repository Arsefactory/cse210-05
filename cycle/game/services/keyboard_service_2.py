# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



from game.location.location import Location
from game.services.keyboard_service import Keyboard_Service
import pyray
class Keyboard_Service_2(Keyboard_Service):
    
    def __init__(self, cell_size):
        super().__init__(cell_size)
        self._cell_size = cell_size
        

   
    def get_direction(self):
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_J):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_L):
            dx = 1

        if pyray.is_key_down(pyray.KEY_I):
            dy = -1

        if pyray.is_key_down(pyray.KEY_K):
            dy = 1

        direction = (dx  , dy )
        # direction = direction.scale(self._cell_size)
        
        return direction