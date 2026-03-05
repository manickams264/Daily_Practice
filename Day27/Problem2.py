class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxi = 0
        current = 0
        window = set()
        start = 0
        for end in range(len(nums)):
            while nums[end] in window or end - start + 1 > k:
                window.remove(nums[start])
                current -= nums[start]
                start += 1
            window.add(nums[end])
            current += nums[end]
            if end - start + 1 == k:
                maxi = max(maxi, current) 
        return maxi