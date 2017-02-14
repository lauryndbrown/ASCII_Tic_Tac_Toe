from ascii_game.player import Player
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
class RandomComputerPlayer(ComputerPlayer):
    def move(self, board):
        return random.choice(board.avalible_moves())
class PerfectComputerPlayer(ComputerPlayer):
    def move(self, board):
        pass
class MixedComputerPlayer(ComputerPlayer):
    def __init__(self, name, value, high_score=0):
        super().__init__(name, value, high_score)
        perfect_player = PerfectComputerPlayer(name, value, high_score) 
        random_player = RandomComputerPlayer(name, value, high_score) 
        self.strategy = [perfect_player, random_player]
    def move(self, board):
        random.choice(self.strategy).move(board)
