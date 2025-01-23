class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(row, col):
            grid[row][col] = "0"

            for r, c in [
                (row, col - 1),
                (row, col + 1),
                (row - 1, col),
                (row + 1, col),
            ]:
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
                    if grid[r][c] == "1":
                        sink(r, c)

        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    cnt += 1
                    sink(r, c)
        return cnt
    
