# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



from game.location.location import Location
import pyray
class Keyboard_Services:
    
    def __init__(self, cell_size):
        self._cell_size = cell_size

   
    def get_direction(self):
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1

        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        direction = (dx , dy )
        # direction = direction.scale(self._cell_size)
        
        return direction