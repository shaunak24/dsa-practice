class Solution:

    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            num = arr[i]
            if num == 0:
                for j in range(len(arr) - 2, i, -1):
                    arr[j + 1] = arr[j]
                if i < len(arr) - 1:
                    arr[i + 1] = 0
                i += 1
            i += 1
        print(arr)


s = Solution()
print(s.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(s.duplicateZeros([1, 2, 3]))
