class Solution:
    def reformat(self, s: str) -> str:
        letters = [char for char in s if char.isalpha()]
        digits = [char for char in s if char.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(digits) > len(letters):
            letters, digits = digits, letters
        result = []
        for index in range(len(digits)):
            result.append(letters[index])
            result.append(digits[index])
        if len(letters) > len(digits):
            result.append(letters[-1])
        return "".join(result)
        