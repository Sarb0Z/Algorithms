
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size=len(prices)
        current_max=0
        max_possible=0
        for i in range(0, size):
            current_max=0
            for j in range(i, size):
                if (prices[j]-prices[i]) > current_max:
                    current_max = prices[j] - prices[i]
            if (current_max>max_possible):
                max_possible=current_max
        
        # for item in max_possible:
        #     if item>max:
        #         max=item
        return max_possible
