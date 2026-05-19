class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find the low
        # Find the high to the right of low
        # Use two pointers
        # One to track low, one to track high to right of low
        l = 0
        r = 0
        max_profit = 0


        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif prices[l] <= prices[r]:
                
                profit = prices[r] - prices[l]

                if profit > max_profit:
                    max_profit = profit

                r += 1

        return max_profit