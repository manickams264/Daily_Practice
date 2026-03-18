class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        length = len(nums)
        answer = 0
        for index1 in range(length):
            for index2 in range(index1 + 1, length):
                for index3 in range(index2 + 1, length):
                    for index4 in range(index3 + 1, length):
                        if nums[index1] + nums[index2] + nums[index3] == nums[index4]:
                            answer += 1
        return answer
        