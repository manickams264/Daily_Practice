class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result=[]
        text=text.split()
        length=len(text)
        for index in range(length):
            if index+1<n and index+2<length:
                if text[i]==first and text[i+1]==second:
                    result.append(text[i+2])
        return result