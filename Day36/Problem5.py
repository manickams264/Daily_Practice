from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        result = -1
        for number in count:
            if count[number] == number:
                result = max(result, number)
        return result
        