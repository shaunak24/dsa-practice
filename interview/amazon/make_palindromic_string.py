def minSwapsRequired(s):
    ans = 0
    n = len(s)
    # Calculate no. of differences
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            ans += 1
    # no solution if diff = odd and length is even
    if ans % 2 == 1 and n % 2 == 0:
        return -1
    # we can resolve diff in half swaps
    return (ans + 1) // 2


print(minSwapsRequired('0100101'))
print(minSwapsRequired('101000'))
print(minSwapsRequired('1100'))
print(minSwapsRequired('1110'))
