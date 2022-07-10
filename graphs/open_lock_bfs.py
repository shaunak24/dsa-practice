from collections import deque


class Solution:

    def getAdjacent(self, node, index, action):
        tmp = list(node)
        if action == 'plus':
            c = '0' if tmp[index] == '9' else str(int(tmp[index]) + 1)
        else:
            c = '9' if tmp[index] == '0' else str(int(tmp[index]) - 1)
        tmp[index] = c
        return ''.join(tmp)

    def openLock(self, deadends, target) -> int:
        vis = set()
        q = deque()
        q.append('0000')

        count = 0
        while len(q) > 0:
            for i in range(len(q)):
                new_node = q.popleft()
                if new_node == target:
                    return count
                if new_node in deadends or new_node in vis:
                    continue
                vis.add(new_node)
                for j in range(len(new_node)):
                    adj_1 = self.getAdjacent(new_node, j, 'plus')
                    adj_2 = self.getAdjacent(new_node, j, 'minus')
                    q.append(adj_1)
                    q.append(adj_2)
            count += 1
        return -1


s = Solution()
print(s.openLock(['0201', '0101', '0102', '1212', '2002'], '0202'))
print(s.openLock(['8888'], '0009'))
print(
    s.openLock(
        ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'],
        '8888'))
