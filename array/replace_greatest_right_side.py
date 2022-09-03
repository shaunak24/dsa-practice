class Solution:

    def replaceElements(self, arr):
        max = -1
        for i in range(len(arr) - 1, -1, -1):
            n = arr[i]
            arr[i] = max
            if n > max:
                max = n
        return arr


s = Solution()
print(s.replaceElements([17, 18, 5, 4, 6, 1]))
print(s.replaceElements([400]))
