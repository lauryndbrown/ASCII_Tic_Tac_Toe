from ascii_game.game_display.display import Display
from ascii_game.game_display.input_tools import *

class TicTacToeDisplay(Display):
    TITLE_OFFSET = 3
    IN_GAME_MENU_OFFSET = 4
    GAME_SCREEN_OFFSET = 7 + TITLE_OFFSET + IN_GAME_MENU_OFFSET 
    SETTINGS_SCREEN_OFFSET = 0 + TITLE_OFFSET + IN_GAME_MENU_OFFSET
    def __init__(self):
        col_size = 50
        super().__init__(col_size)
    def start_menu(self):
        #self.clear_screen()
        #image = Image.open(self.IMAGES+"title.png")
        #ascii_img = self.image_converter.image_to_ascii(image, 300)
        #print(self.center("Tic Tac Toe", self.HR_BOLD))
        #print(ascii_img, end="")
        #print(self.format_HR(' ')) 
        pass
    def move(self):
        row = enter_next_action("Enter 1, 2, or 3 for Row: ", [1,2,3], self)
        col = enter_next_action("Enter 1, 2, or 3 for Column: ", [1,2,3], self)
        return row, col
    def game_screen(self, game):
        self.clear_screen()
        print(self.center("Tic Tac Toe", self.HR_BOLD))
        print(str(game.game_board))
        self.fill_screen(self.GAME_SCREEN_OFFSET)
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
