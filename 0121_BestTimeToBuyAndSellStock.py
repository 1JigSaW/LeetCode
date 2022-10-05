class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1 
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] 
            if prices[left] < prices[right]:
                max_profit = max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit



prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))