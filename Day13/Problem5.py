class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result_string = ''
        for item in s:
            result_string += item[::-1]
            result_string += ' '
        return result_string.strip()
        