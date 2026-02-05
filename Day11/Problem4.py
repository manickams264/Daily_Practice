class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index]==nums[index+1]:
                nums[index]=nums[index]*2
                nums[index+1]=0
        count_zero=nums.count(0)
        list=[]
        for index in range(len(nums)):
            if nums[index]!=0:
                list.append(nums[index])
        for index in range(count_zero):
            list.append(0)
        return list

    