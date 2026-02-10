class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for index1 in range(len(mat)):
            for index2 in range(len(mat[0])):
                if index1 == index2:
                    total += mat[index1][index2]
                elif index1 + index2 == len(mat)-1:
                    total += mat[index1][index2]
        return total        