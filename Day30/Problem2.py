from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for value in range(left, right + 1):
            is_covered = False
            for start, end in ranges:
                if start <= value <= end:
                    is_covered = True
                    break
            if not is_covered:
                return False
        return True
        