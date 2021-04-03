# https://leetcode.com/problems/count-items-matching-a-rule/submissions/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        count = 0

        for listing in items:
            typeItem, colorItem, nameItem = listing

            if ruleKey == "type" and typeItem == ruleValue:
                count += 1
            elif ruleKey == "color" and colorItem == ruleValue:
                count += 1
            elif ruleKey == "name" and nameItem == ruleValue:
                count += 1

        return count