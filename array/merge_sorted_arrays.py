class Solution:

    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)


s = Solution()
print(s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))
