from typing import List
from collections import defaultdict

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = defaultdict(int)
        for index in range(len(nums) - 1):
            if nums[index] == key:
                count[nums[index + 1]] += 1
        return max(count, key=count.get)
        

        