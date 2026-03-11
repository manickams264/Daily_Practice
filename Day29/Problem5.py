from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        for number in nums:
            if abs(number) < abs(answer) or (abs(number) == abs(answer) and number > answer):
                answer = number
        return answer
          