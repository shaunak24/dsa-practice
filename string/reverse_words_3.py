class Solution:

    def reverseWords(self, s: str) -> str:
        ans = ''
        for word in s.split():
            ans += word[::-1] + ' '
        return ans.strip()


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords("God Ding"))