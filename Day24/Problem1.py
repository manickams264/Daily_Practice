class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.isSelfDividing(num):
                result.append(num)
        return result
    def isSelfDividing(self, num):
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                return False
            temp //= 10
        return True        