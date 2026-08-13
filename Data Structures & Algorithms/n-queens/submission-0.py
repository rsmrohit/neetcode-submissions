class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols, dia1, dia2 = set(), set(), set()
        tmp = ["".join(["."] * n) for i in range(n)]
        sols = []

        def backtrack(row):
            nonlocal sols
            nonlocal tmp

            if row == n:
                # print("HI")
                sols.append(tmp.copy())
                return

            for i in range(n):

                if i in cols or row - i in dia1 or row + i in dia2:
                    continue
                
                cols.add(i)
                dia1.add(row - i)
                dia2.add(row + i)

                tmp[row] = tmp[row][:i] + "Q" + tmp[row][i+1:]
                # print(tmp, row)

                backtrack(row + 1)

                cols.remove(i)
                dia1.remove(row - i)
                dia2.remove(row + i)

                tmp[row] = tmp[row][:i] + "." + tmp[row][i+1:]

        backtrack(0)
        return sols

        