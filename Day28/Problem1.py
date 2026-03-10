class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        length = len(s)
        answer = [0] * length
        previous = float('-inf')
        for item in range(length):
            if s[item] == c:
                previous = item
            answer[item] = item - previous
        previous = float('inf')
        for item in range(length - 1, -1, -1):
            if s[item] == c:
                previous = item
            answer[item] = min(answer[item], previous - item)
        return answer
        