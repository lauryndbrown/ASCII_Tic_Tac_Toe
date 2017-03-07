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
class PerfectComputerPlayer(ComputerPlayer):
    """
    More Strategic TicTacToe Player
    """
    NO_WIN = None
    CENTER = (1,1)
    CORNERS = [(0,0),(2,0),(0,2),(2,2)]
    EDGES = [(0,1),(1,0),(2,1),(1,2)]

    def __init__(self, name, value, high_score=0):
        super().__init__(name, value, high_score)
    def move(self, board, turn):
        """
        Picks the best possible move given the avaliable moves
        """
        moves = board.avalible_moves()
        #if self.turn==1:
        #    return self.move_selected(self.CENTER, moves)or self.move_selected(self.CORNERS, moves)
        if turn==2:
            return self.empty_edge(moves) or self.empty_corner(moves)
        
        return self.win(moves, board) or self.block(moves, board) or self.fork(moves, board) or self.block_fork(moves, board) or self.center(moves) or self.opposite_corner(moves, board) or self.empty_corner(moves) or self.empty_edge(moves)
    
    def win(self, moves, board):
        """
        If the player has two in a row place a third to get three in a row
        """
        return self.win_possible(moves, self.value, board)
    def block(self, moves, board):
        """
        If opponent has two in a row, play the third to block
        """
        return self.win_possible(moves, self.get_opponent_value(), board)

    def fork(self, moves, board):
        """
        
        """
        return None
    def block_fork(self, moves, board):
        """
        If opponent can fork, create 2 in a row that the opponent must block.
        """
        return None
    def center(self, moves):
        """
        Returns center move if avaliable
        """
        return self.CENTER if self.CENTER in moves else None
    def opposite_corner(self, moves, board):
        """
        If opponent is in the corner the play the opposite corner
        """
        return None
    def empty_corner(self, moves):
        """
        If there is an empty corner, play it
        """
        return self.move_selected(self.CORNERS, moves)
    def empty_edge(self, moves):
        """
        If there is an empty edge, play it
        """
        return self.move_selected(self.EDGES, moves)
    def move_selected(self, chosen_moves, avaliable_moves):     
        for move in avaliable_moves:
            if move in chosen_moves:
                return move
        return None
    def win_possible(self, moves, value, board):
        """
        Returns the winning move from the list of moves that allows the player with the specified value to win.
        Returns None otherwise.
        """
        for move in moves:
            if board.try_move(move[0],move[1],value):
                return move
        return None
class MixedComputerPlayer(ComputerPlayer):
    def __init__(self, name, value, high_score=0):
        super().__init__(name, value, high_score)
        perfect_player = PerfectComputerPlayer(name, value, high_score) 
        random_player = RandomComputerPlayer(name, value, high_score) 
        self.strategy = [perfect_player, random_player]
    def move(self, board):
        return random.choice(self.strategy).move(board)
