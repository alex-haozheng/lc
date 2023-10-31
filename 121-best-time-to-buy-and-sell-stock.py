"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        # runtime O(n) memspace O(1)
        l, r = 0, 1
        ret = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if prices[r] > prices[l]:
                ret = max(ret, profit)
            else:
                l = r
            r += 1
        return ret
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp solution
        dip, profit = prices[0], 0
        for p in prices:
            dip = min(dip, p)
            profit = max(profit, p - dip)
        return profit