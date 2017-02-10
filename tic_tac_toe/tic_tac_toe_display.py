from ascii_game.game_display.display import Display
from ascii_game.game_display.input_tools import *

class TicTacToeDisplay(Display):
    def __init__(self):
        col_size = 50
        super().__init__(col_size)
    def start_menu(self):
        print("TicTacToe")
    def game_screen(self, game):
        print("game_screen")
    def settings_screen(self, game):
        print("settings")
    def exit_screen(self):
        print("exit")
