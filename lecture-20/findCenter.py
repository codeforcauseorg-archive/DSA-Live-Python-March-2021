# https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        freq = {}

        for [source, target] in edges:

            if source not in freq:
                freq[source] = 0

            if target not in freq:
                freq[target] = 0

            freq[source] += 1
            freq[target] += 1

        n = len(freq)

        for [key, value] in freq.items():
            if value == n - 1:
                return key

        return -1


