class Solution:

    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for curr_index in range(n):
            if stack:
                while stack:
                    prev_index, prev_temp = stack[-1]
                    if temperatures[curr_index] > prev_temp:
                        stack.pop(-1)
                        ans[prev_index] = curr_index - prev_index
                    else:
                        break
            stack.append((curr_index, temperatures[curr_index]))
        return ans


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([30, 60, 90]))
print(s.dailyTemperatures([30, 40, 50, 60]))
