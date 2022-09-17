class Solution:

    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        start_row, end_row = 0, len(matrix) - 1
        start_col, end_col = 0, len(matrix[0]) - 1
        ans = []
        while start_row <= end_row and start_col <= end_col:
            # traverse right
            for i in range(start_col, end_col + 1):
                ans.append(matrix[start_row][i])
            start_row += 1

            # traverse down
            for i in range(start_row, end_row + 1):
                ans.append(matrix[i][end_col])
            end_col -= 1

            # traverse left
            if start_row <= end_row:
                for i in range(end_col, start_col - 1, -1):
                    ans.append(matrix[end_row][i])
            end_row -= 1

            # traverse up
            if start_col <= end_col:
                for i in range(end_row, start_row - 1, -1):
                    ans.append(matrix[i][start_col])
            start_col += 1

        return ans


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(s.spiralOrder([[1, 2, 3, 4]]))
print(s.spiralOrder([[1], [2], [3]]))
print(
    s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                   [13, 14, 15, 16]]))
