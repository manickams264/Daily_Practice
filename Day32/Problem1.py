class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []  
        for i in range(0, len(s), k):
            part = s[i:i + k]
            if len(part) < k:
                part += fill * (k - len(part))
            ans.append(part)
        return ans
        