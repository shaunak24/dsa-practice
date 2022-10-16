from collections import deque

# Time - O(N)
# Space - O(N)


class Solution:

    def shortestSubarray(self, nums) -> int:
        curr_sum, min_len = 0, float('inf')
        q = deque()
        q.append([0, 0])
        for i, num in enumerate(nums):
            curr_sum += num
            #print('curr_sum', curr_sum, q[0][1])
            while q and (curr_sum - q[0][1] >= k):
                min_len = min(min_len, i - q.popleft()[0] + 1)
                #print('q after compress', q)
                #print('curr_sum after compress', curr_sum)
                #print('min_len after compress', min_len)
            while q and curr_sum <= q[-1][1]:
                q.pop()
                #print('q after pop', q)
            q.append([i + 1, curr_sum])
            #print('q after iteration', q)
        return min_len if min_len != float('inf') else -1
