# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        fast = head
        num = 0
        while fast:
            fast = fast.next
            num += 1
            if n == num:
                break
        
        while fast:
            fast = fast.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next



