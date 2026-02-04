class Solution:
    def findComplement(self, num: int) -> int:
        string=bin(num)[2:]
        result=''
        for item in string:
            if item=='1':
                result+='0'
            else:
                result+='1'
        return int(result,2)
        