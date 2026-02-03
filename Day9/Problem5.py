class Solution:
    def bitwiseComplement(self, n: int) -> int:
        string=bin(n)[2:]
        result=''
        for item in string:
            if item=='0':
                result+='1'
            else:
                result+='0'
        return int(result,2)
        