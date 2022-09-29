def getMedianSubarrays(efficiency, k):
    if not efficiency:
        return 0
    length = len(efficiency)
    if length == 1:
        return 1 if efficiency[0] == k else 0
    # Write your code here
    k = efficiency[k - 1]
    ans = 0
    for window in range(1, length, 2):
        i = 0
        while i + window <= length:
            new_arr = efficiency[i:i + window]
            # print(new_arr)
            if len(new_arr) > 1:
                new_arr.sort()
            # print((len(sorted_eff) + 1) // 2 - 1)
            median = new_arr[(len(new_arr) + 1) // 2 - 1]
            if median == k:
                ans += 1
            i += 1
    return ans


print(getMedianSubarrays([5, 3, 1, 4, 7, 7], 4))
print(getMedianSubarrays([1, 2, 3], 1))
print(getMedianSubarrays([4, 1, 2, 3], 3))
print(getMedianSubarrays([4, 4, 1, 2, 3, 3], 1))
