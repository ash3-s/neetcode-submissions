# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        carry = 0
        total = 0
        dummy = ListNode(0)
        d = dummy
        while l1 or l2 or carry:
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = total // 10 
            val = total % 10
            dummy.next = ListNode(val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next
        return d.next
        


