class Solution:

    def twoSum(self, numbers, target: int):
        sum_map = {}  # num:index
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in sum_map:
                return [sum_map[diff], i + 1]
            sum_map[numbers[i]] = i + 1


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([-1, 0], -1))
print(s.twoSum([2, 3, 4], 6))
