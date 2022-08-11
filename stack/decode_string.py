class Solution:

    def decodeString(self, s: str) -> str:

        def update_stk(stk, c):
            if stk:
                stk[-1] += c
            else:
                stk.append(c)

        num_stk = []
        char_stk = []
        opened = True
        for c in s:
            if c.isalpha():
                update_stk(char_stk, c)
            elif c.isnumeric():
                if num_stk and not opened:
                    num_stk[-1] += c
                else:
                    num_stk.append(c)
                    opened = False
            elif c == '[':
                char_stk.append('')
                opened = True
            elif num_stk:
                n = num_stk.pop(-1)
                current = int(n) * char_stk.pop(-1)
                update_stk(char_stk, current)

        return ''.join(char_stk)


s = Solution()
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString("10[leetcode]"))
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))