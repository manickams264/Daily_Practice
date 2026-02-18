class Solution:
    def defangIPaddr(self, address: str) -> str:
        result_string=''
        for item in address:
            if item=='.':
                result_string+='[.]'
            else:
                result_string+=item
        return result_string        