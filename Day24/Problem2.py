class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countBits(x):
            return (bin(x).count('1'), x)
        return sorted(arr, key=countBits)
