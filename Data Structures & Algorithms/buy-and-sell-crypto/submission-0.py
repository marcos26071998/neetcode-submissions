class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        max_profit = 0

        while sell < len(prices):
            if prices[buy]<prices[sell]:
                curr_profit = prices[sell]-prices[buy]
                if curr_profit > max_profit:
                    max_profit = curr_profit
                sell += 1
            else:
                buy = sell
                sell += 1
        return max_profit        