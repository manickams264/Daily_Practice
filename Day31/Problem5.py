class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for index in range(1, len(chars), 2):
            chars[index] = chr(ord(chars[index - 1]) + int(chars[index]))
        return "".join(chars)
        