class Solution:
    def maximumGap(self, numbers: List[int]) -> int:
        if len(numbers) == 1:
            return 0
        numbers.sort()
        max_gap = 0
        for index in range(0, len(numbers) - 1, 1):
            if numbers[index + 1] - numbers[index] > max_gap:
                max_gap = numbers[index + 1] - numbers[index]
        return max_gap
