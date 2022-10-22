# Use only O(rowIndex) extra space


class Solution:

    def getRow(self, rowIndex: int):
        prev = [1]
        for _ in range(rowIndex):
            prev = list(map(lambda x, y: x + y, [0] + prev, prev + [0]))
        return prev


s = Solution()
print(s.getRow(3))
print(s.getRow(0))
print(s.getRow(1))