class Solution:

    def bubbleSort(self, heights):
        hasSwapped = True
        while hasSwapped:
            hasSwapped = False
            for i in range(len(heights) - 1):
                if heights[i] > heights[i + 1]:
                    hasSwapped = True
                    heights[i], heights[i + 1] = heights[i + 1], heights[i]

    def heightChecker(self, heights) -> int:
        count = 0
        tmp = heights[:]
        self.bubbleSort(heights)
        print(heights)
        for i in range(len(heights)):
            if tmp[i] != heights[i]:
                count += 1
        return count


s = Solution()
print(s.heightChecker([1, 1, 4, 2, 1, 3]))
print(s.heightChecker([5, 1, 2, 3, 4]))
print(s.heightChecker([1, 2, 3, 4, 5]))
