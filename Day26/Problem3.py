class Solution:
    def maximum69Number (self, num: int) -> int:
        stack = list(str(num))
        for index in range(len(stack)):
            if stack[index] == '6':
                stack[index] = '9'
                break
        return int(''.join(stack))
        