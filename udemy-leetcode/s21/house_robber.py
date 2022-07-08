class Solution:
    def houseRobber(self, houses):
        n = len(houses)

        if n == 0:
            return 0

        dp = [0] * n
        dp[0] = houses[0]

        for i in range(1, len(houses)):
            if (i == 1):
                dp[i] = max(houses[0], houses[1])
            else:
                dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])

        return dp[-1]


s = Solution()
print(s.houseRobber([1, 2, 3, 1]))
