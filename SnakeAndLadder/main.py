from GameManger import GameManger
from screen_manger import ScreenManger


def main():
    screen = ScreenManger()
    gameManger = GameManger(screen)
    gameManger.add_player('green')
    gameManger.add_player('red')
    screen.screen.update()
    screen.screen.onkeypress(gameManger.start_game, 'space')
    screen.screen.onkeypress(gameManger.rotate_dice_right, 'Right')
    screen.screen.onkeypress(gameManger.rotate_dice_left, 'Left')
    screen.screen.listen()
    screen.screen.mainloop()


if __name__ == '__main__':
    main()
