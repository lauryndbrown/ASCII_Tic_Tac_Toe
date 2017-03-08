from ascii_game.game_display.display import Display
from ascii_game.game_display.input_tools import *
from tic_tac_toe.game_entities import TicTacToe
from tic_tac_toe.player import *
from PIL import Image
import time
import random
import os

class TicTacToeDisplay(Display):
    #Images Directory
    IMAGES = os.path.join("tic_tac_toe","Images")
    #Offsets used to determine the whitespace needed to fill the screen
    TITLE_OFFSET = 3
    IN_GAME_MENU_OFFSET = 4
    GAME_SCREEN_OFFSET = 28 + TITLE_OFFSET + IN_GAME_MENU_OFFSET 
    COMPUTER_MOVE_OFFSET = 1 + GAME_SCREEN_OFFSET 
    SETTINGS_SCREEN_OFFSET = 4 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    def __init__(self):
        col_size = 50
        super().__init__(col_size)
        self._create_ascii_images()
        self._create_board_parts()
        self.computer_thinking = True
    def _create_ascii_images(self):
        """
        Used in __init__ 
        Create Images and Convert Images to ascii
        """
        title_image = Image.open(os.path.join(self.IMAGES, "title.png"))
        x_image = Image.open(os.path.join(self.IMAGES, "x.png"))
        o_image = Image.open(os.path.join(self.IMAGES,"o.png"))
        line_image = Image.open(os.path.join(self.IMAGES,"line.png"))
        vline_image = Image.open(os.path.join(self.IMAGES,"verticle_line.png"))
        self.image_converter.row_incr = 5
        self.image_converter.col_incr = 5
        title_image = self.image_converter.scale_image(title_image, 400)
        o_image = o_image.resize((50,25))
        x_image = x_image.resize((50,25))
        self.ascii_o = self.image_converter.image_to_ascii(o_image)
        self.ascii_x = self.image_converter.image_to_ascii(x_image)
        self.image_converter.invert_chars()
        self.ascii_title = self.image_converter.image_to_ascii(title_image)
        title_offset = (self.get_terminal_col()-80)//2
        title_offset_str = ((" "*title_offset)+'\n')*20
        self.ascii_title = self.image_converter.combine(title_offset_str, self.ascii_title)
    def _create_board_parts(self):
        """
        Used in __init__
        Create Board images and Dictionary Mapping
        """
        self.ascii_empty = ((" "*10)+"\n")*5
        self.ascii_vline = " | \n | \n | \n | \n | \n"
        self.ascii_line ="-"*40 
        self.board = {
                    TicTacToe.EMPTY:list(self.ascii_empty),
                    TicTacToe.O:self.ascii_o,
                    TicTacToe.X:self.ascii_x
                        }    
    def start_menu(self, game):
        """
        Displays Start Menu
        """
        self.clear_screen()
        print(self.ascii_title)
        self._in_game_menu(game.menu)
        self.last_menu = (self.game_screen, (game,))
    def build_board(self, board):
        """
        Builds the Board for display
        """
        def get_col(value, pos):
            if value==TicTacToe.EMPTY:
                empty_col = self.board[value]
                empty_col[28] = str(pos)
                return "".join(empty_col)
            return self.board[value]
        def build_row(values, pos):
            col1 = get_col(values[0], pos)
            col2 = get_col(values[1], pos+1)
            col3 = get_col(values[2], pos+2)
            row_a = self.image_converter.combine(col1, self.ascii_vline)
            row_b = self.image_converter.combine(col2, self.ascii_vline)
            row = self.image_converter.combine(row_a, row_b)
            row = self.image_converter.combine(row,col3)
            row = self.image_converter.combine(self.board_col_offset, row)
            return row, pos+2
        pos = 1
        col_offset = (self.get_terminal_col()-len(self.ascii_line))//2
        self.board_col_offset = ((" "*(col_offset))+'\n')*5 
        self.board_offset = " "*col_offset 
        row1, pos = build_row(board[0], pos)
        row2, pos = build_row(board[1], pos+1)
        row3, pos = build_row(board[2], pos+1)
        
        print(row1, end="")
        print(self.board_offset+self.ascii_line)
        print(row2, end="")
        print(self.board_offset+self.ascii_line)
        print(row3, end="")
    def move(self, moves, game):
        """
        Asks the User for the next Move
        """
        def ask_next_move(message):
            while True:
                response = input(message)
                if response.isdigit():
                    response = int(response)
                if response in range(1,10) and TicTacToe.get_row_col(response) in moves:
                    return response
        def ask_x_or_o(message):
            while True:
                response = input(message).lower()
                if response == TicTacToe.X or response ==TicTacToe.O:
                    return response
        if game.mode == game.STANDARD_MODE:
            message = "You're player {}! Enter 1-9 for Position:".format(game.player_1.value.upper())
            pos = ask_next_move(message)
            row, col = TicTacToe.get_row_col(int(pos))
            return row, col
        elif game.mode == game.WILD_MODE:
            message = "X or O? "
            value = ask_x_or_o(message)
            message = "Enter 1-9 for Position:"
            pos = ask_next_move(message)
            row, col = TicTacToe.get_row_col(int(pos))
            return row, col, value
    def game_screen(self, game, game_over=False):
        """
        Displays the Game Screen
        """
        self.clear_screen()
        print(self.center("Tic Tac Toe", self.HR_BOLD))
        self.build_board(game.game_board.board)
        self.fill_screen(self.GAME_SCREEN_OFFSET)
        if game_over:
            if not game.current_player:
                message ="It's a tie."
            else:
                if game.current_player.is_computer():
                    message ="Sorry. You Lose!"
                else:
                    message ="Congrats Player! You Win!"
            print(self.center(message," "))
        self._in_game_menu(game.menu)
        self.last_menu = (self.game_screen, (game,))
    def computer_move(self, game):
        """
        Plays computer thinking animation
        """
        self.clear_screen()
        print(self.center("Tic Tac Toe", self.HR_BOLD))
        self.build_board(game.game_board.board)
        self.fill_screen(self.COMPUTER_MOVE_OFFSET)
        if self.computer_thinking:
            print("Computer Thinking")
            for _i in range(random.randrange(0,3)):
                print(".")
                time.sleep(1)
    def toggle_computer_thinking(self):
        if self.computer_thinking:
            self.computer_thinking = False
        else:
            self.computer_thinking = True
    def settings_screen(self, game):
        """
        Displays the Settings Screen
        """
        self.clear_screen()
        print(self.center("Settings", self.HR_BOLD))
        print("Game Mode: {}".format(game.mode))   
        print("Computer Thinking Animation: {}".format(ON_OR_OFF[self.computer_thinking]))
        print("Computer Player: Random")
        self.fill_screen(self.SETTINGS_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.settings_screen, (game,))

    def exit_screen(self):
        """
        Displays the Message before the Game Exits
        """
        print(self.center("Thanks for Playing!", ' '))

    def clear_screen(self):
        """
        Clears the screen
        """
        lines = self.get_terminal_lines()
        print(lines*"\n")
