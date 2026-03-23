class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank_map = {}
        for i, num in enumerate(sorted_unique):
            rank_map[num] = i + 1
        return [rank_map[num] for num in arr]
        