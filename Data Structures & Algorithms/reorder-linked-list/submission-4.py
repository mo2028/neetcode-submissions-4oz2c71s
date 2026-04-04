# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val)

        curr = slow.next
        prev = None
        while curr:
            print(curr.val)
            nextNode = curr.next
            curr.next  = prev
            prev = curr
            curr = nextNode

        slow.next = None

        curr = head

        while curr and prev:
            nextCurrNode = curr.next
            nextPrevNode = prev.next

            curr.next = prev
            prev.next = nextCurrNode
            curr = nextCurrNode
            prev = nextPrevNode

        return None


        
            

        
            

        
        