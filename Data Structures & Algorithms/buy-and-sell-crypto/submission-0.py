class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        low, high = float('inf'), float('-inf')

        for i in prices:

            if i < low:
                low = i
                high = low
                continue
            
            profit = max(profit, i-low)
            
        return profit
        