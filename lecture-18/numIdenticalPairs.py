# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        gpairs = 0

        freq = {}

        for item in nums:

            if item in freq:
                gpairs += freq[item]
                freq[item] += 1
            else:
                freq[item] = 1

        return gpairs

