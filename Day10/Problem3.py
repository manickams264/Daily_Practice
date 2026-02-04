class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        buy=prices[0]
        for i in prices:
            current=i-buy
            best=max(best,current)
            buy=min(buy,i)
        return best