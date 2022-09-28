class Solution:

    def removeDuplicates(self, arr):
        # arr.sort()
        i = 1
        while i < len(arr):
            if arr[i] == arr[i - 1]:
                arr[i:] = arr[i + 1:]
            else:
                i += 1
        return arr


s = Solution()
print(s.removeDuplicates([1, 1, 2, 2, 3, 4]))
print(s.removeDuplicates([1]))
print(s.removeDuplicates([1, 2, 4]))