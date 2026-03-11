class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        for item, price in enumerate(cost):
            if item % 3 != 2:   
                total += price
        return total
        