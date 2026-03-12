class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        odd_digits = sorted((digit for digit in digits if digit % 2 == 1), reverse=True)
        even_digits = sorted((digit for digit in digits if digit % 2 == 0), reverse=True)
        odd_index = 0
        even_index = 0
        result_digits = []
        for digit in digits:
            if digit % 2 == 0:
                result_digits.append(str(even_digits[even_index]))
                even_index += 1
            else:
                result_digits.append(str(odd_digits[odd_index]))
                odd_index += 1
        return int("".join(result_digits))
        