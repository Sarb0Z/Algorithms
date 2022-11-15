"""You are given an integer array prices where prices[i] is the price of 
a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve."""

# we must buy at the lowest point
# and sell at the highest point
# if price goes lower bptr keeps track
# if price goes higher tptr keeps track
# the moment prices goes lower from an upward trend we sell the previous day
# profit is tptr price - bptr price

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        tptr=0
        bptr=0
        cptr=0
        while (cptr<len(prices)-1):
            if (prices[cptr]>prices[cptr+1]):
                if (tptr==cptr):
                    profit=profit+(prices[tptr]-prices[bptr])
                bptr=cptr+1
            else:
                tptr=cptr+1
            cptr=cptr+1
        if (tptr==cptr):
            profit=profit+(prices[tptr]-prices[bptr])
        return profit

                

            