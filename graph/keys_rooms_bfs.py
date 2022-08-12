from collections import deque


class Solution:

    def canVisitAllRooms(self, rooms):
        vis = [False for i in range(len(rooms))]
        q = deque()
        q.append(rooms[0])
        vis[0] = True

        while q:
            keys = q.popleft()
            for n in keys:
                if not vis[n]:
                    q.append(rooms[n])
                    vis[n] = True

        return vis.count(False) == 0


s = Solution()
print(s.canVisitAllRooms([[1], [2], [3], []]))
print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
