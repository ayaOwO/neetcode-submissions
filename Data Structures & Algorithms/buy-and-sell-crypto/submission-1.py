class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        buy = prices[0]
        for value in prices[1:]:
            max_diff = max(value - buy, max_diff)
            buy = min(value, buy)
            
        return max_diff

