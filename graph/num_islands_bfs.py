from collections import deque


class Solution:

    def isValid(self, i, j, grid, vis):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and (int(
                grid[i][j]) and not vis[i][j]):
            return True
        return False

    def bfs(self, grid, i, j, vis):
        row = [-1, 0, 0, 1]
        column = [0, 1, -1, 0]

        q = deque()
        q.append((i, j))
        vis[i][j] = True

        while len(q) > 0:
            ai, aj = q.popleft()
            #print('ai, aj: ', ai, aj)
            for n in range(len(row)):
                #print('Co-ordinates: ' + str(ai + row[n]), str(aj + column[n]))
                if self.isValid(ai + row[n], aj + column[n], grid, vis):
                    #print('Valid')
                    q.append((ai + row[n], aj + column[n]))
                    vis[ai + row[n]][aj + column[n]] = True

    def numIslands(self, grid) -> int:
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                #print('Main: ', i, j)
                if int(grid[i][j]) and not vis[i][j]:
                    self.bfs(grid, i, j, vis)
                    count += 1
        return count


s = Solution()
print(
    s.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
                  ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(
    s.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
