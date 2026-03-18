class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row, column = len(grid), len(grid[0])
        answer = 0
        prefix = [[0] * column for _ in range(row)]
        for index1 in range(row):
            for index2 in range(column):
                prefix[index1][index2] = grid[index1][index2]
                if index1 > 0:
                    prefix[index1][index2] += prefix[index1 - 1][index2]
                if index2 > 0:
                    prefix[index1][index2] += prefix[index1][index2 - 1]
                if index1 > 0 and index2 > 0:
                    prefix[index1][index2] -= prefix[index1 - 1][index2 - 1]
                if prefix[index1][index2] <= k:
                    answer += 1
        return answer
        