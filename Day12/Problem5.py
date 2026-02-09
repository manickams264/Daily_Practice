class Solution:
    def toLowerCase(self, s: str) -> str:
        result_string = ''
        for item in s:
            if 65 <= ord(item) <= 90:
                result_string += chr(ord(item)+32)
            else:
                result_string += item
        return result_string