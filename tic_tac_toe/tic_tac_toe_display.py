from ascii_game.game_display.display import Display
from ascii_game.game_display.input_tools import *
from tic_tac_toe.game_entities import TicTacToe
from PIL import Image

class TicTacToeDisplay(Display):
    #Images Directory
    IMAGES = "tic_tac_toe\\Images\\"
    #Offsets used to determine the whitespace needed to fill the screen
    TITLE_OFFSET = 3
    IN_GAME_MENU_OFFSET = 4
    GAME_SCREEN_OFFSET = 28 + TITLE_OFFSET + IN_GAME_MENU_OFFSET 
    SETTINGS_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    def __init__(self):
        col_size = 50
        super().__init__(col_size)
        self._create_ascii_images()
        self._create_board_parts()
    def _create_ascii_images(self):
        """
        Used in __init__ 
        Create Images and Convert Images to ascii
        """
        title_image = Image.open(self.IMAGES+"title.png")
        x_image = Image.open(self.IMAGES+"x.png")
        o_image = Image.open(self.IMAGES+"o.png")
        line_image = Image.open(self.IMAGES+"line.png")
        vline_image = Image.open(self.IMAGES+"verticle_line.png")
        self.image_converter.row_incr = 5
        self.image_converter.col_incr = 5
        title_image = self.image_converter.scale_image(title_image, 400)
        o_image = o_image.resize((50,25))
        x_image = x_image.resize((50,25))
        self.ascii_o = self.image_converter.image_to_ascii(o_image)
        self.ascii_x = self.image_converter.image_to_ascii(x_image)
        self.image_converter.invert_chars()
        self.ascii_title = self.image_converter.image_to_ascii(title_image)
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
        self.clear_screen()
        print(self.ascii_title)
        self._in_game_menu(game.menu)
        self.last_menu = (self.game_screen, (game,))
    def build_board(self, board):
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
            return row, pos+2
        pos = 1
        row1, pos = build_row(board[0], pos)
        row2, pos = build_row(board[1], pos+1)
        row3, pos = build_row(board[2], pos+1)
        print(row1, end="")
        print(self.ascii_line)
        print(row2, end="")
        print(self.ascii_line)
        print(row3, end="")
    def move(self, player_letter):
        def get_row_col(pos):
            row = None
            col = None
            if pos<=3:
                row = 0
            elif pos>3 and pos<=6:
                row = 1
            else:
                row = 2
            if pos%3==0:
                col=2
            elif pos%3==1:
                col=0
            else:
                col=1
            return row, col
        def ask_next_move():
            message = "Player {} Enter 1-9 for Position:".format(player_letter)
            while True:
                response = input(message)
                if response.isdigit():
                    response = int(response)
                if response in range(1,9):
                    return response
        pos = ask_next_move()
        print("pos:", str(pos))
        row, col = get_row_col(int(pos))
        return row, col
    def game_screen(self, game, game_over=False):
        self.clear_screen()
        print(self.center("Tic Tac Toe", self.HR_BOLD))
        self.build_board(game.game_board.board)
        self.fill_screen(self.GAME_SCREEN_OFFSET)
        if game_over:
            message ="Congrats Player {}! You Win!".format(game.player_letter) 
            print(self.center(message," "))
        self._in_game_menu(game.menu)
        self.last_menu = (self.game_screen, (game,))
    def settings_screen(self, game):
        self.clear_screen()
        print(self.center("Settings", self.HR_BOLD))
        self.fill_screen(self.SETTINGS_SCREEN_OFFSET)
        self._in_game_menu(game.menu)
        self.last_menu = (self.settings_screen, (game,))
    def exit_screen(self):
        print(self.center("Thanks for Playing!", ' '))
    def clear_screen(self):
        lines = self.get_terminal_lines()
        print(lines*"\n")
