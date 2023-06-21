class Solution:

    def findUnion(self, arr1, arr2) -> None:
        if len(arr1) == 0 or len(arr2) == 0:
            return arr1 + arr2
        p1, p2 = 0, 0
        union = []
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] <= arr2[p2]:
                if len(union) == 0 or union[-1] != arr1[p1]:
                    union.append(arr1[p1])
                p1 += 1
            else:
                if len(union) == 0 or union[-1] != arr2[p2]:
                    union.append(arr2[p2])
                p2 += 1
        while p1 < len(arr1):
            if union[-1] != arr1[p1]:
                union.append(arr1[p1])
            p1 += 1
        while p2 < len(arr2):
            if union[-1] != arr2[p2]:
                union.append(arr2[p2])
            p2 += 1
        return union

s = Solution()
print(s.findUnion([1, 2, 3], [2, 3, 4]))
print(s.findUnion([1, 2, 3], [1, 2, 3]))
print(s.findUnion([1], [3, 3]))
print(s.findUnion([1], []))
