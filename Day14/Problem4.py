class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums=[(index,nums[index]) for index in range(len(nums))]
        nums=sorted(nums,key=lambda x:x[1])
        result=sorted(nums[-k:],key=lambda x:x[0])
        list=[]
        for item in result:
            list.append(item[1])
        return list