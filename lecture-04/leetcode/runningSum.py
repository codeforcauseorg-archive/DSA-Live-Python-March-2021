# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums):
        for idx in range(1, len(nums)):
            nums[idx] = nums[idx] + nums[idx - 1]

        return nums