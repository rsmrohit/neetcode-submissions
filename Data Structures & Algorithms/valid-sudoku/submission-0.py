class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # all we need to check is for duplicates
        # + ., numbers in all spots

        # Base

        for i in board:
            for j in i:
                if j == '.':
                    continue
                if int(j) <= 9 and int(j) > 0:
                    continue
                return False


        # Dupes

        # all cells will be checked three times
        squares = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2), (2, 2), (2, 1), (1, 2)]
        rows = [(0, i) for i in range(9)]
        cols = [(i, 0) for i in range(9)]

        def grabset(offsets, i_off=0, j_off=0):
            nonlocal board
            return [int(board[i + i_off][j + j_off]) for i, j in offsets if board[i+i_off][j+j_off] != '.']
        
        for c in range(9):
            rowl = grabset(rows, i_off=c)
            if len(rowl) != len(set(rowl)):
                return False
        
        for c in range(9):
            coll = grabset(cols, j_off=c)
            if len(coll) != len(set(coll)):
                return False

        for ci, cj in [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]:
            sql = grabset(squares, i_off=ci, j_off=cj)
            if len(sql) != len(set(sql)):
                return False
        return True
