class Solution:

    def isValid(self, i, j, grid, vis):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and (int(
                grid[i][j]) and not vis[i][j]):
            return True
        return False

    def dfs(self, grid, i, j, vis):
        if self.isValid(i, j, grid, vis):
            vis[i][j] = True
            self.dfs(grid, i + 1, j, vis)
            self.dfs(grid, i - 1, j, vis)
            self.dfs(grid, i, j - 1, vis)
            self.dfs(grid, i, j + 1, vis)

    def numIslands(self, grid) -> int:
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                #print('Main: ', i, j)
                if int(grid[i][j]) and not vis[i][j]:
                    self.dfs(grid, i, j, vis)
                    count += 1
        return count


s = Solution()
print(
    s.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
                  ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(
    s.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                  ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
