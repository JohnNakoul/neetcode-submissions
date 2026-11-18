class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxValue = float('-inf')

        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxValue = max(maxValue, currSum)
        return maxValue


