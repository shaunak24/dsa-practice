def max_platforms(arr, dep):
    max_trains = 0
    for i in range(len(arr)):
        max_tmp = 0
        for j in range(len(dep)):
            if dep[i] > arr[j] and dep[i] < dep[j]:
                max_tmp += 1
        if max_tmp > max_trains:
            max_trains = max_tmp
    return max_trains


print(max_platforms([1, 1.50, 1.20, 2, 2.15, 4], [1.1, 2.2, 3, 2.3, 3.15, 6]))
print(
    max_platforms([1, 1.50, 1.20, 2, 2.15, 4, 4.30, 2],
                  [1.1, 2.2, 3, 2.3, 3.15, 6, 5, 2.30]))
