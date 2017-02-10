from ascii_game.game import Game, Choice
from ascii_game.player import Player
from tic_tac_toe.game_entities import TicTacToe
from tic_tac_toe.tic_tac_toe_display import TicTacToeDisplay

class TicTacToeGame(Game):
    #Menu Names
    GAME_MENU_NAME = "Game"
    SETTINGS_MENU_NAME = "Settings"
    #Option Names
    BACK_OPTION = "Back"
    def __init__(self, display, player1, player2):
        super().__init__(display, player1, player2)
        self.game_board = TicTacToe()
        game_menu = []
        settings_menu = []
        #Game Menu
        game_menu.append(Choice("End Game",self.end_game, None, None))
        game_menu.append(Choice("Settings",self.display.settings_screen, (self,), self.SETTINGS_MENU_NAME))
        #Settings Menu
        settings_menu.append(Choice(self.BACK_OPTION,self.display.game_screen, (self,), self.GAME_MENU_NAME))
        #settings_menu.append(Choice("Toggle 1 or 2 Players",self.display.game_screen, (self,), self.GAME_MENU))
        self.menus = {self.GAME_MENU_NAME:game_menu, self.SETTINGS_MENU_NAME:settings_menu}
        #Current game menu is pointed to by self.menu
        self.menu = game_menu
        #Because the game has just started the previous menu is None
        self.prev_menu = None
    def start(self):
        self.display.start_menu()
        super().start()
    def end_game(self):
        self.display.exit_screen()
if __name__=="__main__":
    display = TicTacToeDisplay()
    player1 = Player("Player1")
    player2 = Player("Player2")
    game = TicTacToeGame(display, player1, player2)
    game.start()

