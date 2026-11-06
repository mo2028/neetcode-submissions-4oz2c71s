# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxSoFar):
            if not root:
                return 0

            res = 0
            if root.val >= maxSoFar:
                res +=1

            maxSoFar = max(maxSoFar, root.val)

            left = helper(root.left, maxSoFar)
            right = helper(root.right, maxSoFar)

            res += left + right
            return res
        return helper(root, root.val)
        