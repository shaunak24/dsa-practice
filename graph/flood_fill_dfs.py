class Solution:

    def is_valid(self, i, j, image, init):
        if i >= 0 and j >= 0 and i < len(image) and j < len(
                image[0]) and image[i][j] == init:
            return True
        return False

    def dfs(self, i, j, image, vis, init, color):
        row = [0, 0, 1, -1]
        col = [1, -1, 0, 0]
        vis[i][j] = True
        image[i][j] = color

        for n in range(len(row)):
            ar = i + row[n]
            ac = j + col[n]
            if self.is_valid(ar, ac, image, init) and not vis[ar][ac]:
                self.dfs(ar, ac, image, vis, init, color)

    def floodFill(self, image, sr: int, sc: int, color: int):
        vis = [[False for i in range(len(image[0]))]
               for j in range(len(image))]
        init = image[sr][sc]
        self.dfs(sr, sc, image, vis, init, color)
        return image


s = Solution()
print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
