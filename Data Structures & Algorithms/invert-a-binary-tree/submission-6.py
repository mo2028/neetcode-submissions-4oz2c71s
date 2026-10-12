# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # this is my trying without looking thte solution after i just copied to get the hang of it 
        # case where it is an empty tree or it is a child of a leaf node

        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left or node.right:
                node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

            
            







        