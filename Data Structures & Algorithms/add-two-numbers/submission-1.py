# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode()
        resCurr = resHead
        leftover = 0
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            sum = l1Val + l2Val + leftover
            if sum >= 10:
                leftover = 1
                sum -= 10
            else:
                leftover = 0
            
            resCurr.next = ListNode(sum) 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            resCurr = resCurr.next
        
        if leftover > 0:
            resCurr.next = ListNode(1)
        
        return resHead.next 