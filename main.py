from GameManger import GameManger
from screen_manger import ScreenManger

import turtle


def main():
    screen = ScreenManger()
    gameManger = GameManger(screen)
    gameManger.add_player('green')
    gameManger.add_player('red')
    screen.screen.update()
    screen.screen.onkeypress(gameManger.start_game, 'space')
    screen.screen.listen()
    screen.screen.mainloop()
