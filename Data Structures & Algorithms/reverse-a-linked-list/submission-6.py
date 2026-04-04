# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        if not curr or not curr.next:
            return curr

        newHead = self.reverseList(curr.next)
        curr.next.next  = curr
        curr.next = None

        return newHead
            

        