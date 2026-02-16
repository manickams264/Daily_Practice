class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = 0
        zeros_allowed = 1   
        while right_pointer < len(nums):
            if nums[right_pointer] == 0:
                zeros_allowed -= 1
            right_pointer += 1
            if zeros_allowed < 0:
                if nums[left_pointer] == 0:
                    zeros_allowed += 1
                left_pointer += 1        
        return right_pointer - left_pointer - 1
