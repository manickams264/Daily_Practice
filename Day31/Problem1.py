class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish_in(time_limit: int) -> bool:
            reduced_height = 0
            for worker_time in workerTimes:
                max_layers = (math.isqrt(1 + (8 * time_limit) // worker_time) - 1) // 2
                reduced_height += max_layers
                if reduced_height >= mountainHeight:
                    return True
            return False
        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if can_finish_in(mid):
                right = mid
            else:
                left = mid + 1
        return left