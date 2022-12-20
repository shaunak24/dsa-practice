class Solution:

    def sortColors(self, nums) -> None:
        count_map = {}
        for n in nums:
            if n not in count_map:
                count_map[n] = 0
            count_map[n] += 1
        ball, i = 0, 0
        print(count_map)
        while i < len(nums):
            if ball > 2:
                break
            if ball not in count_map or count_map[ball] == 0:
                ball += 1
                continue
            nums[i] = ball
            count_map[ball] -= 1
            i += 1
        print(nums)


s = Solution()
# print(s.sortColors([2, 0, 2, 1, 1, 0]))
# print(s.sortColors([2, 0, 1]))
# print(s.sortColors([2]))
print(s.sortColors([2, 0, 2, 1, 1, 0]))
