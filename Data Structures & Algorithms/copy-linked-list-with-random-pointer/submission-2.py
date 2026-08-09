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
        oldToCopy = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            c = oldToCopy[curr]
            c.next = oldToCopy[curr.next] if  curr.next != None else None
            c.random = oldToCopy[curr.random] if curr.random != None else None
            curr = curr.next
        curr = head
        return oldToCopy[head] if head != None else None