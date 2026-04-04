"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # map
        oldToNew = {None : None}
        curr = head

        # go over and make all the nodes
        while curr :
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]

