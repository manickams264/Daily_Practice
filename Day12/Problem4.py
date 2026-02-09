class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for item in operations:
            if item[-1].isdigit():
                result.append(int(item))
            elif item == '+':
                number1 = result[-1]
                number2 = result[-2]
                result.append(number1 + number2)
            elif item == 'D':
                number = result[-1]
                result.append(number*2)
            elif item == 'C':
                result.remove(result[-1])
        return sum(result)
        