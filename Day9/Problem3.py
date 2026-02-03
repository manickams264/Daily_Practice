class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=''
        for item in address:
            if item=='.':
                result+='[.]'
            else:
                result+=item
        return result        