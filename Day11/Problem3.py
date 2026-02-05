class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count=0
        for index1 in range(len(words)):
            length=len(words[index1])
            for index2 in range(index1+1,len(words)):
                if words[index1]==words[index2][:length] and words[index1]==words[index2][-length:]:
                    count+=1
        return count

        