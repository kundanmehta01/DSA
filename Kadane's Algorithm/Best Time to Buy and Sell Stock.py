# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current=prices[0]
        best=0
        ans=0

        for i in range(1,len(prices)):
            if prices[i]<current:
                current=prices[i]
            else:
                ans= prices[i]-current

            best=max(best,ans)
        return best
            