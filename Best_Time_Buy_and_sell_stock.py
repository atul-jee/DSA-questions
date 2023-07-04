# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#Leetcode Best time to sell and bu stcok
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_price=0
        for ele in prices:
            min_price=min(min_price,ele)
            max_price=max(max_price,ele-min_price)
        return max_price