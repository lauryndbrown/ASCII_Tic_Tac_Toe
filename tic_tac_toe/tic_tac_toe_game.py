from ascii_game.game import Game, Choice
from tic_tac_toe.game_entities import TicTacToe
from tic_tac_toe.tic_tac_toe_display import TicTacToeDisplay
from tic_tac_toe.player import *

class TicTacToeGame(Game):
    #Menu Names
    START_MENU_NAME = "Start"
    GAME_MENU_NAME = "Game"
    GAME_OVER_MENU_NAME = "Game Over"
    SETTINGS_MENU_NAME = "Settings"
    #Option Names
    BACK_OPTION = "Back"
    #Win/Lose
    GAME_OVER = "game over"
    def __init__(self, display, player1, player2):
        super().__init__(display, player1, player2)
        self.game_board = TicTacToe()
        start_menu = []
        game_menu = []
        game_over_menu = []
        settings_menu = []
        #Start Menu
        start_menu.append(Choice("Start Game",self.display.game_screen, (self,), self.GAME_MENU_NAME))
        start_menu.append(Choice("Exit TicTacToe",self.end_game, None, None))
        #Game Menu
        game_menu.append(Choice("End Game",self.end_current_game, (), self.START_MENU_NAME))
        game_menu.append(Choice("Settings",self.display.settings_screen, (self,), self.SETTINGS_MENU_NAME))
        game_menu.append(Choice("Move", self.move, (), None))
        #Game Over Menu
        game_over_menu.append(Choice("End Game",self.end_current_game, (), self.START_MENU_NAME))
        game_over_menu.append(Choice("Settings",self.display.settings_screen, (self,), self.SETTINGS_MENU_NAME))
        game_over_menu.append(Choice("New Game", self.new_game, (), None))
        #Settings Menu
        settings_menu.append(Choice(self.BACK_OPTION,self.display.game_screen, (self,), self.GAME_MENU_NAME))
        #settings_menu.append(Choice("Toggle 1 or 2 Players",self.display.game_screen, (self,), self.GAME_MENU))
        self.menus = {self.START_MENU_NAME:start_menu, self.GAME_MENU_NAME:game_menu, self.SETTINGS_MENU_NAME:settings_menu, self.GAME_OVER_MENU_NAME:game_over_menu}
        #Current menu is pointed to by self.menu
        self.menu = start_menu
        #Because the game has just started the previous menu is None
        self.prev_menu = None
        self.current_player = self.player_1
    def start(self):
        self.display.start_menu(self)
        super().start()
    def move(self):
        def computer_player():
            if issubclass(self.current_player.__class__, ComputerPlayer):
                row, col = self.current_player.move(self.game_board)    
                self.game_board.move(row, col, self.current_player.value)
                self._switch_player()
        def check_game_over():
            if self.game_board.has_won():
                self.menu = self.menus[self.GAME_OVER_MENU_NAME]
                self.display.game_screen(game, self.GAME_OVER)
            else:
                self._switch_player()
                computer_player()
                self.display.game_screen(game)
        row, col = self.display.move(self.current_player.value)
        self.game_board.move(row, col, self.current_player.value)
        check_game_over()
    def _switch_player(self):
        if self.current_player==self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1
    def new_game(self):
        self.game_board.empty_board()
        self.display.game_screen(self)
    def end_game(self):
        self.display.exit_screen()
    def end_current_game(self):
        self.game_board.empty_board()
        self.display.start_menu(self)
if __name__=="__main__":
    display = TicTacToeDisplay()
    player1 = TicTacToePlayer("Player1",TicTacToe.X)
    player2 = RandomComputerPlayer("Player2", TicTacToe.O)
    game = TicTacToeGame(display, player1, player2)
    game.start()

