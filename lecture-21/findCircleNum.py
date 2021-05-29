# https://leetcode.com/problems/number-of-provinces/submissions/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        p_map = [None] * len(isConnected);

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c] == 1:
                    Solution.union(r, c, p_map)

        count = 0
        for parent in p_map:
            if parent == None:
                count += 1

        return count

    @classmethod
    def find(cls, current, p_map):
        while p_map[current] != None:
            current = p_map[current]
        return current

    @classmethod
    def union(cls, first, second, p_map):

        rep_f = Solution.find(first, p_map)
        rep_s = Solution.find(second, p_map)

        if rep_f != rep_s:
            p_map[rep_f] = rep_s
            return True
        else:
            return False
