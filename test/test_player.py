import unittest

from tic_tac_toe.player import *

class TicTacToePlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = PerfectComputerPlayer("Perfect",TicTacToe.X)
    def test_move_empty_board(self):
        board = TicTacToe()
        win_possible = self.player.win_possible(board.avalible_moves(), self.player.value, board)
        self.assertEqual(win_possible,self.player.NO_WIN)
        self.assertEqual(self.player.move(board), (1,1))
