# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley

from game.director.director import Director
from game.services.video_service import Video_Service

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = 'Cycle'


def main():
    # start the game
    
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)

    video_service = Video_Service(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director("keyboard_service", video_service)
    director.start_game()


if __name__ == '__main__':
    main()
