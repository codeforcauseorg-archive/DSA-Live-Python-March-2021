# https://leetcode.com/problems/regions-cut-by-slashes/

class Solution:
    def regionsBySlashes(self, grid):

        p_map = []

        for i in range(len(grid)):
            row = [None] * (2 * len(grid))
            p_map.append(row)

        edges = []
        for ridx, row in enumerate(grid):
            cidx = 0
            while(cidx < len(row)):
                if row[cidx] == " ":
                    edges.append(((ridx, cidx*2), (ridx, cidx*2+1)))
                    edges.append(((ridx, cidx*2), (ridx, cidx*2-1)))
                    edges.append(((ridx, cidx*2), (ridx+1, cidx*2)))
                    edges.append(((ridx, cidx*2+1), (ridx+1, cidx*2+1)))
                    edges.append(((ridx, cidx*2+1), (ridx, cidx*2+2)))
                    cidx += 1
                elif row[cidx] == "/":
                    edges.append(((ridx, cidx * 2), (ridx, cidx * 2 - 1)))
                    edges.append(((ridx, cidx * 2 + 1), (ridx + 1, cidx * 2 + 1)))
                    edges.append(((ridx, cidx * 2 + 1), (ridx, cidx * 2 + 2)))
                    cidx += 1
                else:
                    edges.append(((ridx, cidx * 2), (ridx, cidx * 2 - 1)))
                    edges.append(((ridx, cidx * 2), (ridx + 1, cidx * 2)))
                    edges.append(((ridx, cidx * 2 + 1), (ridx, cidx * 2 + 2)))
                    cidx += 1

        for (start, end) in edges:
            Solution.union(start, end, p_map)

        print(p_map)
        count = 0
        for r in range(len(p_map)):
            for c in range(2*len(p_map)):
                if p_map[r][c] == None:
                    count += 1

        return count




    @classmethod
    def find(cls, current, p_map):
        row, col = current
        while p_map[row][col] != None:
            row, col = p_map[row][col]

        return row, col

    @classmethod
    def union(cls, first, second, p_map):

        r, c = first
        if r < 0 or r >= len(p_map) or c < 0 or c >= 2*len(p_map):
            return False

        r, c = second
        if r < 0 or r >= len(p_map) or c < 0 or c >= 2 * len(p_map):
            return False



        rep_f = Solution.find(first, p_map)
        rep_s = Solution.find(second, p_map)

        if rep_f != rep_s:
            p_map[rep_f[0]][rep_f[1]] = rep_s
            return True
        else:
            return False


sol = Solution()
grid = [" /","/ "]
print(sol.regionsBySlashes(grid))


