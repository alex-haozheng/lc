'''
You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.
'''
    
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ret = 0
        for r, rowList in enumerate(board):
            if 'R' in rowList:
                c = rowList.index('R')
                break
        
        # rook coordinates (r,c)
        for i in range(r-1, -1, -1):
            if board[i][c] != '.':
                if board[i][c] == 'p':
                    ret += 1
                break

        for i in range(r+1, len(board)):
            if board[i][c] != '.':
                if board[i][c] == 'p':
                    ret += 1
                break

        for i in range(c-1, -1, -1):
            if board[r][i] != '.':
                if board[r][i] == 'p':
                    ret += 1
                break

        for i in range(c+1, len(board[0])):
            if board[r][i] != '.':
                if board[r][i] == 'p':
                    ret += 1
                break

        return ret