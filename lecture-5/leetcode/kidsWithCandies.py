# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        maxVal = 0

        for count in candies:
            if count > maxVal:
                maxVal = count

        sol = []

        for count in candies:
            sol.append((count + extraCandies) >= maxVal)

        return sol