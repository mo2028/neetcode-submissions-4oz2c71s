# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length = length+1
            curr = curr.next
        # print(length)

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nodeToRemove = length - (n)
        counter = 0
        while curr:
            if counter == nodeToRemove:
                curr.next = curr.next.next
                break

            counter = counter + 1
            curr = curr.next
        return dummy.next  