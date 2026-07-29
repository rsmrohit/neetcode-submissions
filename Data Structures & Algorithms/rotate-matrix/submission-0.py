class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # you gotta figure out how to map each value to the new one, we can figure out an algo
        # to assign each one or we can say that a right rotation is the same as 
        # transformation = (x, y) -> (-x, y) then (-x, y) -> (y, -x)
        n = len(matrix)
        # Transformation 1:

        for j in range(n):
            for i in range(n // 2):
                # print(i, j ,n)
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        
        # Transformation 2:
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)