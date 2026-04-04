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

        curr = head
        currTwo = head
        oldNewMap = {None: None}

        while curr:
            newNode = Node(curr.val)
            oldNewMap[curr] = newNode
            curr = curr.next

        while currTwo:
            newNode = oldNewMap[currTwo]
            newNode.next = oldNewMap[currTwo.next]
            newNode.random = oldNewMap[currTwo.random]
            currTwo = currTwo.next

        return oldNewMap[head]



        