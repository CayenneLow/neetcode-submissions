# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head != None:
            if head.val == -9999:
                return True
            head.val = -9999
            head = head.next
        return False