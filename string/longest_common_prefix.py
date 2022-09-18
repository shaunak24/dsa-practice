class Solution:

    def longestCommonPrefix(self, strs) -> str:
        ans = ''
        # Sort and compare the first and last element
        strs.sort()
        for i, j in zip(strs[0], strs[-1]):
            if i != j:
                return ans
            ans += i
        return ans


s = Solution()
print(s.longestCommonPrefix(['flower', 'flow', 'flight']))
print(s.longestCommonPrefix(['dog', 'racecar', 'car']))
print(s.longestCommonPrefix(['flower', 'flower', 'flower']))
print(s.longestCommonPrefix(['ab', 'a']))
