class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dictionary = {}
        for index in range(len(s)):
            dictionary[indices[index]] = s[index]
        result_string = ''
        for item in sorted(dictionary.keys()):
            result_string += dictionary[item]  
        return result_string        
            
        