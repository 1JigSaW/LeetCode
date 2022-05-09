class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = 3
        columns = 3
        start = 0
        start2 = 0
        while rows < 10:
            d = []
            for i in range(start2, rows):
                for j in range(start, columns):
                    if board[i][j] not in d:
                        d.append(board[i][j])
                    elif board[i][j] == '.':
                        pass
                    else:
                        return False
            if columns == 9:
                start2 += 3
                rows += 3
                start = 0
                columns = 3
            else:
                columns += 3
                start += 3
        d = []
        for i in range(len(board)):
            for j in board[i]:
                if j not in d:
                    d.append(j)
                elif j == '.':
                    pass
                else:
                    return False
            d = []
        d = []
        c = 0
        while c != len(board):
            for i in range(len(board[0])):
                if board[i][c] not in d:
                    d.append(board[i][c])
                elif board[i][c] == '.':
                    pass
                else:
                    return False
            d = []
            c += 1
        return True
        