class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        zero_rows = []
        zero_cols = []
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if grid[row_index][col_index] == 0:
                    zero_rows.append(row_index)
                    zero_cols.append(col_index)
        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                if row_index in zero_rows or col_index in zero_cols:
                    grid[row_index][col_index] = 0
