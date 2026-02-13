class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p=max_p=r=nums[0]
        for i in range(1,len(nums)):
            candidates=(nums[i],max_p*nums[i],min_p*nums[i])
            temp=max(candidates)
            min_p=min(candidates)
            max_p=temp
            r=max(r,max_p)
        return r
        