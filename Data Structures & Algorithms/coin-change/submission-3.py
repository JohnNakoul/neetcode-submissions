class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount+1):
            for coin in coins:
                if current_amount >= coin:
                    remaining = current_amount - coin
                    dp[current_amount] = min(dp[current_amount], 1 + dp[remaining])
        
        if dp[amount] == amount+1:
            return -1
        
        return dp[amount]