class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list=[]
        for index1 in range(len(nums)-1):
            for index2 in range(index1+1,len(nums)):  
                if nums[index1]+nums[index2]==target:
                    list.append(index1)
                    list.append(index2)
                    return list    