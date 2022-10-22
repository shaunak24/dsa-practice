class Solution:

    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        ans = ''
        for i in range(len(s) - 1, -1, -1):
            if s[i]:
                ans += s[i] + ' '
        return ans.strip()


s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world  "))
print(s.reverseWords("a good   example"))