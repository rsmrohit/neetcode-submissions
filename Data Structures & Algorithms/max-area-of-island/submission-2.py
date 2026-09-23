class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # we'll remove islands that we've found so we dont double count them
        row = len(grid)
        col = len(grid[0])

        # def remove_island(i: int, j: int) -> int:

        #     for c in card:
        #         i, j
        #         if 

        max_island = 0
        cardinals = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    # max_island = max(remove_island(i, j), max_island)
                    max_island = max(max_island, count)
                    q.append((i, j))
                    grid[i][j] = 0
                    count = 0
                    # print("Found Island at ", i, j)
                
                while q:
                    coords = q.pop(0)
                    # grid[coords[0]][coords[1]] = 0
                    count += 1
                    for c in cardinals:
                        i_c, j_c = coords[0] + c[0], coords[1] + c[1]
                        # print("Checking ", i_c, j_c)
                        if i_c in range(row) and j_c in range(col):
                            if grid[i_c][j_c] == 1:
                                # print("Works")
                                q.append((i_c, j_c))
                                grid[i_c][j_c] = 0

        return max(max_island, count)

                