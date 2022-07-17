# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root):
        ans = []

        def sol(root, ans):
            if not root:
                return
            sol(root.left, ans)
            ans.append(root.val)
            sol(root.right, ans)

        sol(root, ans)
        return ans
