class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer, seen = set(), set()
        for index in range(len(s)-9):
            dna = s[index:index+10]
            if dna in seen:
                answer.add(dna)
            else:
                seen.add(dna)
        return list(answer)