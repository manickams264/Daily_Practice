class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for index1 in range(k):
            min_element=min(nums)
            for index2 in range(len(nums)):
                if nums[index2]==min_element:
                    nums[index2]=min_element*multiplier
                    break
        return nums

        