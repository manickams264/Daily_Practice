from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_index = (i * n + j + k) % total
                new_row = new_index // n
                new_col = new_index % n
                result[new_row][new_col] = grid[i][j]
        return result
        