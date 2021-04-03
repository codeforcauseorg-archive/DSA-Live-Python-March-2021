# https://leetcode.com/problems/destination-city/submissions/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        sourcetarget = {}

        for source, target in paths:
            sourcetarget[source] = target

        initial = paths[0][0]

        while initial in sourcetarget:
            initial = sourcetarget[initial]

        return initial