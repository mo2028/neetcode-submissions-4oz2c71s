# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        

        q = deque()
        q.append(root)
        answer = []

        while len(q) > 0:
            level = []
            qLen = len(q)
            while qLen > 0:
                nextElement  = q.popleft()
                level.append(nextElement.val)
                if nextElement.left:
                    q.append(nextElement.left)
                if nextElement.right:
                    q.append(nextElement.right)
                qLen -= 1
            answer.append(level)
        return answer










            











            
        