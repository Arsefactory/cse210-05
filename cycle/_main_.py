# Names of People in Group: 
# Dawson Packer
# John Pischke
# Logan Crossley

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
    cast = Cast()
    
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    player = Player(x, 560)
    cast.set_player(player)

    keyboard_service = Keyboard_Service(CELL_SIZE)
    video_service = Video_Service(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == '__main__':
    main()