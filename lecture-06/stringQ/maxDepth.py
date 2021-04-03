# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

class Solution:
    def maxDepth(self, s: str) -> int:

        maxVal = 0
        count = 0

        for ch in s:
            if ch == "(":
                count += 1
                if count > maxVal:
                    maxVal = count
            elif ch == ')':
                count -= 1

        return maxVal

