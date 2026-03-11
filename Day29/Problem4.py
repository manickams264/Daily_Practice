from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        length = len(matrix)
        required = set(range(1, length + 1))
        for index1 in range(length):
            row = set(matrix[index1])
            col = set(matrix[index2][index1] for index2 in range(length))
            if row != required or col != required:
                return False
        return True