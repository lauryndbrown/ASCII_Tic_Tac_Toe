from ascii_game.player import Player
from tic_tac_toe.game_entities import TicTacToe
from abc import ABC, abstractmethod
import random
class TicTacToePlayer(Player):
    def __init__(self, name, value, high_score=0):
        super().__init__(name, high_score)
        self.value = value
class ComputerPlayer(TicTacToePlayer):
    def __init__(self, name, value, high_score=0):
        super().__init__(name, value, high_score)
    @abstractmethod
    def move(self, board):
        pass
    def get_opponent_value(self):
        if self.value==TicTacToe.X:
            return TicTacToe.O
        return TicTacToe.X
class RandomComputerPlayer(ComputerPlayer):
    def move(self, board):
        return random.choice(board.avalible_moves())
class PerfectComputerPlayer(ComputerPlayer):
    NO_WIN = None
    CENTER = (1,1)
    CORNERS = [(0,0),(2,0),(0,2),(2,2)]
    def move(self, board):
        moves = board.avalible_moves()
        win = self.win_possible(moves, self.value, board)
        if win:
            return win
        opponent_win = self.win_possible(moves, self.get_opponent_value(), board)
        if opponent_win:
            return opponent_win
        if self.CENTER in moves:
            return self.CENTER
        for move in self.CORNERS:
            if move in moves:
                return move
        return random.choice(board.avalible_moves())
        
    def win_possible(self, moves, value, board):
        for move in moves:
            if board.try_move(move[0],move[1],value):
                return move
        return self.NO_WIN
class MixedComputerPlayer(ComputerPlayer):
    def __init__(self, name, value, high_score=0):
        super().__init__(name, value, high_score)
        perfect_player = PerfectComputerPlayer(name, value, high_score) 
        random_player = RandomComputerPlayer(name, value, high_score) 
        self.strategy = [perfect_player, random_player]
    def move(self, board):
        return random.choice(self.strategy).move(board)
