import unittest

from tic_tac_toe.game_entities import TicTacToe

class TicTacToeTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def _board_empty(self, board):
         for row in board.board:
            for cell in row:
                self.assertEqual(cell, TicTacToe.EMPTY)
    def test_init(self):
        board = TicTacToe()
        self.assertEqual(len(board.board), 3)
        self.assertEqual(len(board.board[0]), 3)
        self.assertEqual(len(board.board[1]), 3)
        self.assertEqual(len(board.board[2]), 3)
        self._board_empty(board)
    def test_empty_board(self):
        board = TicTacToe()
        board.board = [[ TicTacToe.X,TicTacToe.X,TicTacToe.X],
         [ TicTacToe.X,TicTacToe.X,TicTacToe.X],
         [ TicTacToe.X,TicTacToe.X,TicTacToe.X]]
        board.empty_board()
        self._board_empty(board)
    def test_move(self):
        tictactoe = TicTacToe()
        tictactoe.move(2,2,TicTacToe.X)
        tictactoe.move(0,1,TicTacToe.O)
        tictactoe.move(1,0,TicTacToe.X)
        self.assertEqual(tictactoe.board[2][2],TicTacToe.X)
        self.assertEqual(tictactoe.board[0][1],TicTacToe.O)
        self.assertEqual(tictactoe.board[1][0],TicTacToe.X)

    def test_has_won_cols(self):
        board = TicTacToe()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.X,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.X,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.X,TicTacToe.EMPTY,TicTacToe.EMPTY]]
        self.assertEqual(board.has_won(),True)
        board.empty_board()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.O,TicTacToe.EMPTY],
         [ TicTacToe.EMPTY,TicTacToe.O,TicTacToe.EMPTY],
         [ TicTacToe.EMPTY,TicTacToe.O,TicTacToe.EMPTY]]
        self.assertEqual(board.has_won(),True)
        board.empty_board()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X]]
        self.assertEqual(board.has_won(),True)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.O],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X]]
        self.assertEqual(board.has_won(),False)

    def test_has_won_rows(self):
        board = TicTacToe()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.X,TicTacToe.X,TicTacToe.X],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.EMPTY]]
        self.assertEqual(board.has_won(),True)
        board.empty_board()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.O,TicTacToe.O,TicTacToe.O],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.EMPTY]]
        self.assertEqual(board.has_won(),True)
        board.empty_board()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.X,TicTacToe.X,TicTacToe.X]]
        self.assertEqual(board.has_won(),True)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X],
         [ TicTacToe.X,TicTacToe.O,TicTacToe.O],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X]]
        self.assertEqual(board.has_won(),False)
    def test_has_won_diagonals(self):
        board = TicTacToe()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.X,TicTacToe.EMPTY,TicTacToe.EMPTY],
         [ TicTacToe.EMPTY,TicTacToe.X,TicTacToe.EMPTY],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X]]
        self.assertEqual(board.has_won(),True)
        board.empty_board()
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.O],
         [ TicTacToe.EMPTY,TicTacToe.O,TicTacToe.EMPTY],
         [ TicTacToe.O,TicTacToe.EMPTY,TicTacToe.EMPTY]]
        self.assertEqual(board.has_won(),True)
        board.empty_board()
        self.assertEqual(board.has_won(),False)
        board.board = [
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.O],
         [ TicTacToe.EMPTY,TicTacToe.X,TicTacToe.EMPTY],
         [ TicTacToe.O,TicTacToe.X,TicTacToe.X]]
        self.assertEqual(board.has_won(),False)
        board.board = [[ TicTacToe.X,TicTacToe.EMPTY,TicTacToe.X],
         [ TicTacToe.X,TicTacToe.O,TicTacToe.O],
         [ TicTacToe.EMPTY,TicTacToe.EMPTY,TicTacToe.X]]
        self.assertEqual(board.has_won(),False)
    def test_str_(self):
        board = TicTacToe()
        board.board = [[ TicTacToe.X,TicTacToe.X,TicTacToe.X],
         [ TicTacToe.X,TicTacToe.X,TicTacToe.X],
         [ TicTacToe.X,TicTacToe.X,TicTacToe.X]]
        board_str = """\nx | x | x\n----------\nx | x | x\n----------\nx | x | x\n"""
        self.assertEqual(board_str,str(board))
       
