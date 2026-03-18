class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous = -1
        for index, number in enumerate(nums):
            if number == 1:
                if previous != -1 and index - previous - 1 < k:
                    return False
                previous = index
        return True
        