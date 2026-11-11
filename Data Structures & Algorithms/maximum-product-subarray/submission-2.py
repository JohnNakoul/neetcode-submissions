class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curMax = 1
        curMin = 1

        for i in nums:
            if i == 0:
                curMax = 1
                curMin = 1
                continue

            temp = i * curMax
            curMax = max(i * curMax, i * curMin, i)
            curMin = min(temp, i * curMin, i)
            ans = max(ans, curMax, curMin)

        return ans