# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        c = ListNode()
        c.next = head
        dummy = c
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        l = 0
        curr = head
        prev = dummy
        while l != length - n:
            l += 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr.next = None
        return dummy.next
        
