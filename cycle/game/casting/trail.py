# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley



import random
from game.casting.trail_chunk import Trail_Chunk


class Trail:
    
    def __init__(self):
       self.trail_chunks = []
       self.trail_color = (random.randrange(255), random.randrange(255),random.randrange(255))

    def add_chunk(self, chunk):
        self.trail_chunks.append(chunk)


   

