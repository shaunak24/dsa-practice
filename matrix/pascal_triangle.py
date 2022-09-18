# explanation: Any row can be constructed using the offset sum of the previous row. Example:

#     1 3 3 1 0
#  +  0 1 3 3 1
#  =  1 4 6 4 1


class Solution:

    def generate(self, numRows):
        ans = [[1]]
        for i in range(1, numRows):
            ans.append(
                list(map(lambda x, y: x + y, ans[-1] + [0], [0] + ans[-1])))
        return ans[:numRows]


s = Solution()
print(s.generate(5))
print(s.generate(1))
print(s.generate(0))