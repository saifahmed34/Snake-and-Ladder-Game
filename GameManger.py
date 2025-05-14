from random import randint
from time import sleep

from Constants import *
from cell import Cell
from cmaeraTurtle import CameraTurtle
from dieRoller import DieRoller
from player import Player
from score_board import ScoreBoard
from winnerscreen import WinnerScreen


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

    def draw_cell_number(self):
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
        self.draw_cell_number()

    def add_player(self, player_color):
        self.players.append(Player(self.grid[-1].xcor(), self.grid[-1].ycor(), (N_CELLS * M_CELLS) - 1, player_color))

    def update_screen_numbers_and_score_board(self):
        self.draw_cell_number()
        list_of_players = []
        list_of_players_position = []
        for player in self.players:
            list_of_players.append(player.player_color)
            list_of_players_position.append((N_CELLS * M_CELLS) - player.cell_idx)
        self.score_board.show(list_of_players, list_of_players_position)

    def start_game(self):
        if self.game_running:
            print("game is already running")
            return
        self.game_running = True
        cur_player = self.players[self.player_idx]

        CameraTurtle.move_camera(cur_player.xcor(), cur_player.ycor())
        self.update_screen_numbers_and_score_board()
        rnd_number_move = 0
        for _ in range(randint(4, 10)):
            rnd_number_move = self.die_roller.roll()
            self.screen.screen.update()
            sleep(SCREEN_UPDATE_RATE + .4)
        if cur_player.cell_idx - rnd_number_move >= 0:
            for _ in range(rnd_number_move):
                cur_player.cell_idx -= 1
                cell = self.grid[cur_player.cell_idx]
                cur_player.goto(cell.xcor(), cell.ycor())
                CameraTurtle.move_camera(cur_player.xcor(), cur_player.ycor())
                self.update_screen_numbers_and_score_board()
                self.screen.screen.update()
                sleep(SCREEN_UPDATE_RATE + .3)
            if cur_player.cell_idx == 0:
                winner = WinnerScreen()
                winner.show_winner(cur_player.player_color)
                self.game_running = False
                return
        self.player_idx = (self.player_idx + 1) % len(self.players)
        self.game_running = False
