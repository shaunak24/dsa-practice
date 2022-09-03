class Solution:

    def validMountainArray(self, arr):
        i, n = 0, len(arr)
        # slope up
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        # peak can't be 1st (only decreasing) or last (only increasing)
        if i == 0 or i == n - 1:
            return False
        # slope down
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1


s = Solution()
print(s.validMountainArray([2, 1]))
print(s.validMountainArray([3, 5, 5]))
print(s.validMountainArray([0, 3, 2, 1]))
