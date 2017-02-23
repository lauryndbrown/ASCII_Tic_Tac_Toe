import unittest

from tic_tac_toe.player import *

class TicTacToePlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = PerfectComputerPlayer("Perfect",TicTacToe.O)
        self.opponent = TicTacToePlayer("Opponent",TicTacToe.X)
        self.corners =  [(0,0),(2,0),(0,2),(2,2)]
    def test_move_empty_board(self):
        board = TicTacToe()
        win_possible = self.player.win_possible(board.avalible_moves(), self.player.value, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        self.assertEqual(self.player.move(board), (1,1))
    def test_first_move(self):
        board = TicTacToe()
        board.move((1,1), self.opponent.value)
        win_possible = self.player.win_possible(board.avalible_moves(), self.player.value, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        self.assertEqual(self.player.move(board) in self.corners, True)
        self.assertEqual(win_possible,self.player.NO_WIN)
    def test_win_possible_cols(self):
        board = TicTacToe()
        player_val = self.player.value
        opponent_val = self.opponent.value
        empty = TicTacToe.EMPTY
        board.board = [
         [ player_val,empty,empty],
         [ player_val,empty,empty],
         [ empty,empty,empty]]
        win_possible = self.player.win_possible(board.avalible_moves(),player_val, board)
        self.assertEqual(win_possible,(2,0))
        win_possible = self.player.win_possible(board.avalible_moves(), opponent_val, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        board.board = [
         [ empty,empty,empty],
         [ opponent_val,empty,empty],
         [ opponent_val,empty,empty]]
        win_possible = self.player.win_possible(board.avalible_moves(),player_val, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        win_possible = self.player.win_possible(board.avalible_moves(), opponent_val, board)
        self.assertEqual(win_possible,(0,0))

    def test_win_possible_row(self):
        board = TicTacToe()
        player_val = self.player.value
        opponent_val = self.opponent.value
        empty = TicTacToe.EMPTY
        board.board = [
         [ empty,empty,empty],
         [ player_val,player_val,empty],
         [ empty,empty,empty]]
        win_possible = self.player.win_possible(board.avalible_moves(),player_val, board)
        self.assertEqual(win_possible,(1,2))
        win_possible = self.player.win_possible(board.avalible_moves(), opponent_val, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        board.board = [
         [ empty,empty,empty],
         [ empty,opponent_val,opponent_val],
         [ empty,empty,empty]]
        win_possible = self.player.win_possible(board.avalible_moves(),player_val, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        win_possible = self.player.win_possible(board.avalible_moves(), opponent_val, board)
        self.assertEqual(win_possible,(1,0))

