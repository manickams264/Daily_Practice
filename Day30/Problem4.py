from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current_number = 1
        index = 0
        while k > 0:
            if index < len(arr) and arr[index] == current_number:
                index += 1
            else:
                k -= 1
                if k == 0:
                    return current_number
            current_number += 1
        