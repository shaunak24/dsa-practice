from typing import OrderedDict


class Solution:

    def findDiagonalOrder(self, mat):
        d = OrderedDict()
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if (i + j) not in d:
                    d[i + j] = []
                d[i + j].append(mat[i][j])
        for s in d.keys():
            if s % 2 == 0:
                ans.extend(d[s][::-1])
            else:
                ans.extend(d[s])
        return ans


s = Solution()
print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.findDiagonalOrder([[1, 2], [3, 4]]))
