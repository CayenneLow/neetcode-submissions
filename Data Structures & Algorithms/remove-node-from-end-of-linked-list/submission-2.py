# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        i = 0
        # this is the node to the RIGHT
        right = None
        while len(stack) > 0 and i < (n - 1):
            right = stack.pop()
            i += 1
        curr = None
        if len(stack) > 0:
            curr = stack.pop()
        left = None
        if len(stack) > 0:
            left = stack.pop()

        if left:
            left.next = right
        else:
            return right
        
        if len(stack) > 0:
            return stack[0]
        return left

        
        