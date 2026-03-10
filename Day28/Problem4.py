from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        current = 0
        count = 0
        for number in arr:
            current += number
            if current == target:
                count += 1
                current = 0
        return count >= 3        