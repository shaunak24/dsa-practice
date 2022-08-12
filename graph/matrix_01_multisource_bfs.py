# Multi-source BFS
# Standard BFS is slower than Brute-Force as for each cell we need to perform one BFS iteration
# In Multi-source, we put all 0's in queue and start updating distance for their neighbours

from collections import deque


class Solution:

    def is_valid(self, i, j, mat):
        if i >= 0 and j >= 0 and i < len(mat) and j < len(mat[0]):
            return True
        return False

    def updateMatrix(self, mat):
        row = [0, 0, 1, -1]
        col = [1, -1, 0, 0]
        inf = float('inf')
        ans = [[inf for i in range(len(mat[0]))] for j in range(len(mat))]
        q = deque()

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    ans[i][j] = 0

        while q:
            ai, aj = q.popleft()
            for n in range(len(row)):
                ar = ai + row[n]
                ac = aj + col[n]
                if self.is_valid(ar, ac, mat):
                    if ans[ar][ac] > ans[ai][aj] + 1:
                        ans[ar][ac] = ans[ai][aj] + 1
                        q.append((ar, ac))
        return ans


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(s.updateMatrix([[0], [1]]))
# print(
#     s.updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
#                     [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#                     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
#                     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
#                     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
#                     [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#                     [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
#                     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#                     [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
#                     [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]))
