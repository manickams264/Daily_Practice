class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        temp = []
        for item in nums:
            if temp and item == temp[-1] + 1:
                temp.append(item)
            else:
                if temp:
                    if len(temp) == 1:
                        ans.append(str(temp[0]))
                    else:
                        ans.append((str(temp[0]), str(temp[-1])))
                temp = [item]
        if temp:
            if len(temp) == 1:
                ans.append(str(temp[0]))
            else:
                ans.append((str(temp[0]), str(temp[-1])))
        dummy = []
        for item in ans:
            if isinstance(item, tuple):
                dummy.append('->'.join(item))
            else:
                dummy.append(item)
        return dummy
    