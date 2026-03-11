class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_element = min(nums)
        max_element = max(nums)
        count = 0
        for number in nums:
            if min_element < number < max_element:
                count += 1
        return count
        