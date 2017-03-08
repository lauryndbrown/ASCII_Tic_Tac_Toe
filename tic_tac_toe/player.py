from ascii_game.player import Player
from tic_tac_toe.game_entities import TicTacToe
from abc import ABC, abstractmethod
import random
from abc import abstractmethod
"""
Contains the Various Player types for the TicTacToe Game
"""
class TicTacToePlayer(Player):
    """
    General TicTacToe Player
    """
    def __init__(self, name, high_score=0):
        super().__init__(name, high_score)
    @abstractmethod
    def is_computer(self):
        pass
class StandardTicTacToePlayer(TicTacToePlayer):
    """
    Used for The Human In Standard play
    """
    def __init__(self, name, value, high_score=0):
        super().__init__(name, high_score)
        self.value = value

    def is_computer(self):
        return False
class WildTicTacToePlayer(TicTacToePlayer):
    """
    Used for The Human In Wild Play
    """
    def is_computer(self):
        return False
class WildComputerPlayer(WildTicTacToePlayer):
    """
    Used for Random Computer In Wild Play
    """
    def __init__(self, name, high_score=0):
        super().__init__(name, high_score)
    def move(self, board, turn):
        value = random.choice([board.X, board.O])
        row, col = random.choice(board.avalible_moves())
        return row, col, value
    def is_computer(self):
        return True
class StandardComputerPlayer(StandardTicTacToePlayer):
    """
    TicTacToe Computer Player
    """
    @abstractmethod
    def move(self, board, turn):
        pass
    def get_opponent_value(self):
        if self.value==TicTacToe.X:
            return TicTacToe.O
        return TicTacToe.X
    def is_computer(self):
        return True
class RandomComputerPlayer(StandardComputerPlayer):
    """
    Random Standard TicTacToe Player
    """
    def move(self, board, turn):
        return random.choice(board.avalible_moves())

