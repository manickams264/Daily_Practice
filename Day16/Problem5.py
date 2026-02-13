class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums.sort()
        max_gap=0
        for index in range(0,len(nums)-1,1):
            if nums[index+1]-nums[index]>max_gap:
                max_gap=nums[index+1]-nums[index]
        return max_gap
        