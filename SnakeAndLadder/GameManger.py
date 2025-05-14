from random import randint
from time import sleep

from Constants import *
from cell import Cell
from cmaeraTurtle import CameraTurtle
from dieRoller import DieRoller
from player import Player
from score_board import ScoreBoard
from winnerscreen import WinnerScreen

level = {
    2: 12,  # ladder
    8: 26,  # ladder
    19: 38,  # ladder
    21: 82,  # ladder
    28: 53,  # ladder
    36: 57,  # ladder
    51: 72,  # ladder
    71: 92,  # ladder
    78: 98,  # ladder
    87: 94,  # ladder

    16: 6,  # snake
    47: 26,  # snake
    49: 11,  # snake
    56: 53,  # snake
    62: 19,  # snake
    64: 60,  # snake
    74: 32,  # snake
    89: 68,  # snake
    95: 24,  # snake
    99: 80  # snake
}


class GameManger:
    def __init__(self, screen):
        self.screen = screen
        self.grid = []
        self.players = []
        self.die_roller = DieRoller()
        self.draw_cells()
        self.wait_player_to_press = True
        self.player_idx = 0
        self.game_running = False
        self.score_board = ScoreBoard(SCORE_BOARD_START_X, SCORE_BOARD_START_Y)

    def set_wait_player_to_false(self):
        print("set wait player to false")
        self.wait_player_to_press = False

    def draw_cell_numbers(self):
        idx = N_CELLS * N_CELLS
        for cell in self.grid:
            cell.write_number(idx)
            idx -= 1

    def draw_cells(self):
        self.grid.clear()
        x = START_DRAW_X
        y = START_DRAW_Y
        reverse = False
        tmp_list = []
        for row in range(N_CELLS):
            # self.grid.append([])
            for col in range(M_CELLS):
                cell = Cell(x, y, 'gray')
                tmp_list.append(cell)
                x += PLAYER_SIZE + MARGIN

            if reverse:
                tmp_list.reverse()
            self.grid.extend(tmp_list)
            tmp_list.clear()
            reverse = not reverse
            x = START_DRAW_X
            y -= PLAYER_SIZE + MARGIN

        convert_reverse = lambda position: (N_CELLS * M_CELLS) - position - 1

        for cell, cell_connection in level.items():
            tmp_cell = convert_reverse(cell)
            tmp_cell_connection = convert_reverse(cell_connection)

            self.grid[tmp_cell].linked_to = tmp_cell_connection
            if cell < cell_connection:
                # ladder
                self.grid[tmp_cell].ladder_shape()
            else:
                self.grid[tmp_cell].snake_shape()

        self.draw_cell_numbers()

    def add_player(self, player_color):
        self.players.append(Player(self.grid[-1].xcor(), self.grid[-1].ycor(), player_color))

    def update_screen_numbers_and_score_board(self):
        self.draw_cell_numbers()
        list_of_players = []
        list_of_players_position = []
        for player in self.players:
            list_of_players.append(player.player_color)
            list_of_players_position.append((N_CELLS * M_CELLS) - player.cell_idx)
        self.score_board.show(list_of_players, list_of_players_position)

    def start_game(self):
        # to make sure that only one thread of game runs
        if self.game_running:
            print("game is already running")
            return

        self.game_running = True

        # select the curunt player
        cur_player = self.players[self.player_idx]

        # focuse camera on player
        CameraTurtle.move_camera(cur_player.xcor(), cur_player.ycor())
        self.update_screen_numbers_and_score_board()

        # make dice animation
        rnd_number_move = 0
        for _ in range(randint(4, 10)):
            rnd_number_move = self.die_roller.roll()
            self.screen.screen.update()
            sleep(SCREEN_UPDATE_RATE + .4)

        # check if the next player movent is valid or not
        if cur_player.cell_idx - rnd_number_move >= 0:
            # move animation
            for _ in range(rnd_number_move):
                cur_player.cell_idx -= 1
                cell = self.grid[cur_player.cell_idx]
                cur_player.goto(cell.xcor(), cell.ycor())
                CameraTurtle.move_camera(cur_player.xcor(), cur_player.ycor())
                self.update_screen_numbers_and_score_board()
                self.screen.screen.update()
                sleep(SCREEN_UPDATE_RATE + .3)

            # check if player is the winner
            if cur_player.cell_idx == 0:
                winner = WinnerScreen()
                winner.show_winner(cur_player.player_color)
                self.game_running = False
                return
            # check if player is on snake or ladder cell
            elif self.grid[cur_player.cell_idx].is_snake_or_ladder:
                # extract linked cell index
                target_cell_idx = self.grid[cur_player.cell_idx].linked_to
                target_cell = self.grid[target_cell_idx]

                # move the cur player to link of the snake or ladder
                cur_player.cell_idx = target_cell_idx
                cur_player.goto(target_cell.xcor(), target_cell.ycor())

                # foucse camera on player
                CameraTurtle.move_camera(cur_player.xcor(), cur_player.ycor())
                self.update_screen_numbers_and_score_board()
                self.screen.screen.update()

        self.player_idx = (self.player_idx + 1) % len(self.players)
        self.game_running = False

    def rotate_dice_right(self):
        self.die_roller.rotate_dice_right()
        self.screen.screen.update()

    def rotate_dice_left(self):
        self.die_roller.rotate_dice_left()
        self.screen.screen.update()
