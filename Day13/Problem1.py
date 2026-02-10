class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        first_pointer = 0
        second_pointer = 1
        count = 0
        while first_pointer < second_pointer:
            if second_pointer == len(nums):
                return count
            if nums[first_pointer] == nums[second_pointer] and first_pointer < second_pointer:
                count += 1
            if second_pointer == len(nums)-1:
                first_pointer += 1
                second_pointer = first_pointer
            second_pointer += 1

        