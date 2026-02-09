class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        first_pointer = 0
        second_pointer = 1
        while first_pointer < second_pointer:
            if second_pointer == len(nums):
                return False
            if nums[first_pointer] == nums[second_pointer] and abs(first_pointer-second_pointer) <= k:
                return True
            if second_pointer == len(nums)-1:
                first_pointer += 1
                second_pointer = first_pointer
            second_pointer += 1

            

        