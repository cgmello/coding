class Stocks:
    def maxProfit(self, prices):
        ans = 0
        buyPrice = float("inf")
        for price in prices:
            if price < buyPrice:
                buyPrice = price  # best buy
            else:
                ans = max(ans, price - buyPrice)  # best sell ?
        return ans


s = Stocks()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
