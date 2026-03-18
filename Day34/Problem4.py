class Solution:
    def maxPower(self, s: str) -> int:
        answer = 1
        current = 1
        for index in range(1, len(s)):
            if s[index] == s[index - 1]:
                current += 1
            else:
                current = 1
            answer = max(answer, current)
        return answer
        