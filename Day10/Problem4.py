class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for item in nums:
            if nums.count(item) == 1:
                return item