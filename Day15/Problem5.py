class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result_string = ''
        string = s.split()
        string = string[:k]
        for item in string:
            result_string += item
            result_string += ' '
        return result_string.strip()
