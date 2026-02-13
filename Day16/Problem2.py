class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        target_sum = 0
        nums.sort()
        for first_index in range(len(nums) - 2):
            left_pointer = first_index + 1
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                current_sum = (nums[first_index] + nums[left_pointer] + nums[right_pointer])
                if current_sum == target_sum:
                    result_set.add((nums[first_index],nums[left_pointer],nums[right_pointer]))
                    right_pointer -= 1
                    left_pointer += 1
                elif current_sum < target_sum:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return list(result_set)
