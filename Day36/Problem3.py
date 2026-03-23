class Solution:
    def sortString(self, s: str) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        res = []
        while len(res) < len(s):
            for index in range(26):
                if count[index] > 0:
                    res.append(chr(index + ord('a')))
                    count[index] -= 1
            for index in range(25, -1, -1):
                if count[index] > 0:
                    res.append(chr(index + ord('a')))
                    count[index] -= 1
        return "".join(res)
        