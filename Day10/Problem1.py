class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_string = ''
        for item in s:
            if item.isalpha():
                result_string += item
        if result_string.lower() == result_string[::-1].lower():
            return True
        else:
            return False
        