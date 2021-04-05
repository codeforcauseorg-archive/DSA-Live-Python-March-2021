# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums, n):
        sol = []

        for i in range(n):
            sol.append(nums[i])
            sol.append(nums[n + i])

        return sol