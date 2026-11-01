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
        memory = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            memory[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = memory.get(curr)
            next = memory.get(curr.next)
            random = memory.get(curr.random)
            copy.next = next
            copy.random = random
            curr = curr.next
        return memory.get(head)