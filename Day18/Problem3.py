class Solution:
    def longestOnes(self, numbers: List[int], max_zero_flips: int) -> int:
        left = 0
        right = 0
        while right < len(numbers):
            if numbers[right] == 0:
                max_zero_flips -= 1
            right += 1
            if max_zero_flips < 0:
                if numbers[left] == 0:
                    max_zero_flips += 1
                left += 1
        return right - left
