class Solution:

    def dominantIndex(self, nums):
        max = (-1, -1)  # Index, Value
        second_max = -1
        for i in range(len(nums)):
            if nums[i] > max[1]:
                second_max = max[1]
                max = (i, nums[i])
            elif nums[i] > second_max:
                second_max = nums[i]
        # print(max, second_max)
        return max[0] if max[1] >= second_max * 2 else -1


s = Solution()
print(s.dominantIndex([3, 6, 1, 0]))
print(s.dominantIndex([1, 2, 3, 4]))
