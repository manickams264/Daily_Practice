class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best=0
        buy=prices[0]
        for item in prices:
            current=item-buy
            best=max(best,current)
            buy=min(buy,item)
        return best     
            
        