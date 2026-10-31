# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)

        answer = []

        while len(q) > 0:
            qlen = len(q)
            while qlen > 0:
                poped = q.popleft()
                if qlen == 1:
                    answer.append(poped.val)
                if poped.left:
                    q.append(poped.left)
                if poped.right:
                    q.append(poped.right)
                qlen -= 1

        return answer


