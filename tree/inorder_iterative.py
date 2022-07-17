# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root):
        ans = []
        stack = []
        node = root
        while True:
            if not node:
                if stack:
                    n = stack.pop(-1)
                    ans.append(n.val)
                    node = n.right
                else:
                    break
            else:
                stack.append(node)
                node = node.left
        return ans
