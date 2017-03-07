"""
Game Entities for ASCII Tic Tac Toe
Note Game Utilizes Default Player Class
"""

class TicTacToe:
    """
    Class containing game logic to Tic-Tac-Toe 
    """
    EMPTY = ""
    X = "x"
    O = "o"
    def __init__(self):
        self.board = [
                        [TicTacToe.EMPTY, TicTacToe.EMPTY, TicTacToe.EMPTY],
                        [TicTacToe.EMPTY, TicTacToe.EMPTY, TicTacToe.EMPTY],
                        [TicTacToe.EMPTY, TicTacToe.EMPTY, TicTacToe.EMPTY]
                    ]
    def empty_board(self):
        """
        Set every position in the board to EMPTY
        """
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                self.board[row][col] = TicTacToe.EMPTY 
    def get_pos_value(self, pos):
        """
        Given a position 1-9 return the corresponding 
        value at the row and column. 
        """
        row, col = self.get_row_col(pos)
        return self.board[row][col]
    def get_row_col(pos):
        """
        Given a position 1-9 return the corresponding
        row and column
        """
        row = None
        col = None
        if pos<=3:
            row = 0
        elif pos>3 and pos<=6:
            row = 1
        else:
            row = 2
        if pos%3==0:
            col=2
        elif pos%3==1:
            col=0
        else:
            col=1
        return row, col
    def try_move(self, row, col, val):
        """
        Given a position and a specified value,
        The board is temporarily set to the given value and checks to see if there is a winner. 
        If the position is not empty or if the move does not result in a winner, it returns false.
        """
        if self.board[row][col]==self.EMPTY:
            self.board[row][col] = val
            winner = self.has_won()
            self.board[row][col] = self.EMPTY
            return winner
        return False
            
    def move(self, pos, val):
        """
        Given a position which can be an int 1-9 or a tuple containing (row, col) 
        Set the value of the board at the postion to the given value
        """
        if isinstance(pos, int):
            row, col = get_row_col(pos)
        else:
            row, col = pos[0], pos[1]
        if val!=TicTacToe.EMPTY and val!=TicTacToe.X and val!=TicTacToe.O:
            raise ValueError("Invalid value")
        try:
            self.board[row][col] = val
        except:
            raise ValueError
    
    def has_won(self):
        """
        Checks to see if there is a winner.
        """
        def rows_same():
            row1 = self.board[0][0]==self.board[0][1]==self.board[0][2]
            row1 = row1 and self.board[0][0]!=self.EMPTY
            row2 = self.board[1][0]==self.board[1][1]==self.board[1][2]
            row2 = row2 and self.board[1][0]!=self.EMPTY
            row3 = self.board[2][0]==self.board[2][1]==self.board[2][2]
            row3 = row3 and self.board[2][0]!=self.EMPTY
            return row1 or row2 or row3
        def cols_same():
            col1 = self.board[0][0]==self.board[1][0]==self.board[2][0]
            col1 = col1 and self.board[0][0]!=self.EMPTY
            col2 = self.board[0][1]==self.board[1][1]==self.board[2][1]
            col2 = col2 and self.board[0][1]!=self.EMPTY
            col3 = self.board[0][2]==self.board[1][2]==self.board[2][2]
            col3 = col3 and self.board[0][2]!=self.EMPTY
            return col1 or col2 or col3

        def same_diagonal():
            row1 = self.board[0][0]==self.board[1][1]==self.board[2][2]
            row1 = row1 and self.board[0][0]!=self.EMPTY
            row2 = self.board[0][2]==self.board[1][1]==self.board[2][0]
            row2 = row2 and self.board[0][2]!=self.EMPTY
            return row1 or row2
            
        return rows_same() or cols_same() or same_diagonal()
    def avalible_moves(self):
       """
       Returns a list of the avaliable moves.
       """
       return [(row, col) for row in range(len(self.board)) for col in range(len(self.board[row])) if self.board[row][col]==self.EMPTY ]
    def __str__(self):
        s = """\n{} | {} | {}\n----------\n{} | {} | {}\n----------\n{} | {} | {}\n""".format(self.board[0][0], self.board[0][1], self.board[0][2], self.board[1][0], self.board[1][1], self.board[1][2], self.board[2][0], self.board[2][1], self.board[2][2])
       
        return s

    def __repr__(self):
        self.__str__()
        
