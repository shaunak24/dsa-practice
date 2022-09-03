class Solution:

    def checkIfExist(self, arr):
        for n in arr:
            if n == 0 and arr.count(0) > 1:
                return True
            if n != 0 and n * 2 in arr:
                return True
        return False


s = Solution()
# print(s.checkIfExist([10, 2, 5, 3]))
print(s.checkIfExist([-2, 0, 10, -19, 4, 6, -8]))
# print(s.checkIfExist([7, 1, 14, 11]))
# print(s.checkIfExist([3, 1, 7, 11]))
