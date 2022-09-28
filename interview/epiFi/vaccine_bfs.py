#!/bin/python3

from collections import deque


def bfs(def_num, node_map, status_map):
    count = 0
    q = deque()
    for neigh in node_map[def_num]:
        q.append(neigh)

    while q:
        for i in range(len(q)):
            neigh = q.popleft()
            if status_map[neigh] == 3:
                count += 1
                return count
            for n in node_map[neigh]:
                q.append(n)
        count += 1
    return count


def findMinimumTime(centre_nodes, centre_from, centre_to, status):
    print(centre_nodes, centre_from, centre_to, status)
    node_map = {}  # node:adj
    deficient, status_map = set(), {}
    for i in range(len(centre_from)):
        n_from = centre_from[i]
        n_to = centre_to[i]
        print(i, n_from, n_to)
        if n_from not in node_map.keys():
            node_map[n_from] = []
        if n_to not in node_map.keys():
            node_map[n_to] = []
        node_map[n_from].append(n_to)
        node_map[n_to].append(n_from)
        if status[n_from - 1] == 1:
            deficient.add(n_from)
        if status[n_to - 1] == 1:
            deficient.add(n_to)
        status_map[n_from] = status[n_from - 1]

    min_time = 0
    for def_num in deficient:
        count = bfs(def_num, node_map, status_map)
        min_time = max(count, min_time)

    print(node_map)
    print(deficient, status_map)
    return min_time


print(
    findMinimumTime(6, [1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 1],
                    [3, 2, 1, 2, 1, 2]))
print(
    findMinimumTime(6, [1, 1, 1, 2, 3, 3, 5, 4], [2, 4, 3, 4, 4, 5, 6, 6],
                    [3, 2, 3, 1, 2, 1]))