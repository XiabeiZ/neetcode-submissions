class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0, 0

        while sell < len(prices):
            if prices[buy] <= prices[sell]:
                res = max(res, prices[sell] - prices[buy])
                sell += 1
            else:
                buy = sell
        
        return res