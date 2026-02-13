class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [[] for _ in range(length + 1)]
        dp[length] = [[]]
        for begin in range(length - 1, -1, -1):
            for end in range(begin + 1, length + 1):
                candidate = s[begin:end]
                if candidate == candidate[::-1]:
                     for each in dp[end]:
                         new_each = [candidate]
                         new_each.extend(each)
                         dp[begin].append(new_each)
        return dp[0]  