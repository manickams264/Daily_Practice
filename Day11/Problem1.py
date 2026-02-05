class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        index1=0
        index2=index1+2
        count=0
        while index2<len(nums):
            if nums[index1]+nums[index2]==nums[index1+1]/2:
                count+=1
            index1+=1
            index2+=1
        return count

        