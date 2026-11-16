class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # An odd total cannot be divided equally.
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[current_sum] is True if we can create current_sum.
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for current_sum in range(target, num - 1, -1):
                dp[current_sum] = (
                    dp[current_sum] or dp[current_sum - num]
                )

        return dp[target]