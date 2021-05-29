class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        p_map = {}

        for i in range(1, len(edges) + 1):
            p_map[i] = None

        for edge in edges:
            start, end = edge
            if not Solution.union(start, end, p_map):
                return edge

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
