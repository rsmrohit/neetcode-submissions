class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        seen = [[False] * cols for _ in range(rows)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        d = 0
        i = j = 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[i][j])
            seen[i][j] = True
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            if not (0 <= ni < rows and 0 <= nj < cols) or seen[ni][nj]:
                d = (d + 1) % 4  # turn right
                ni, nj = i + dirs[d][0], j + dirs[d][1]
            i, j = ni, nj

        return res