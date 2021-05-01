# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        count = 0
        solution = []

        for ch in S:
            if ch == "(":
                if count > 0:
                    solution.append("(")

                count += 1

            else:

                if count > 1:
                    solution.append(")")

                count -= 1

        return "".join(solution)
