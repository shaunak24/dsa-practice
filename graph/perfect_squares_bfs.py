from collections import deque


class Solution:

    def numSquares(self, n: int) -> int:
        vis = set()
        q = deque()
        q.append(n)
        vis.add(n)

        count = 0
        while len(q) > 0:
            for i in range(len(q)):
                curr_num = q.popleft()
                if curr_num == 0:
                    return count

                for j in range(curr_num):
                    diff = curr_num - j * j
                    if diff < 0:
                        break
                    if diff not in vis:
                        q.append(diff)
                        vis.add(diff)
            count += 1
        return count


s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(1))