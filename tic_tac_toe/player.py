from ascii_game.player import Player
from tic_tac_toe.game_entities import TicTacToe
from abc import ABC, abstractmethod
import random
"""
Contains the Various Player types for the TicTacToe Game
"""
class TicTacToePlayer(Player):
    """
    General TicTacToe Player
    Used for The Human player
    """
    def __init__(self, name, value, high_score=0):
        super().__init__(name, high_score)
        self.value = value
class ComputerPlayer(TicTacToePlayer):
    """
    TicTacToe Computer Player
    All Computer players inherit from this Class
    """
    @abstractmethod
    def move(self, board, turn):
        pass
    def get_opponent_value(self):
        if self.value==TicTacToe.X:
            return TicTacToe.O
        return TicTacToe.X
class RandomComputerPlayer(ComputerPlayer):
    """
    Random TicTacToe Player
    """
    def move(self, board, turn):
        return random.choice(board.avalible_moves())

