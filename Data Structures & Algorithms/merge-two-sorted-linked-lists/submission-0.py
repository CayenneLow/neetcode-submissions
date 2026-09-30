# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        newCurr = newHead
        curr1 = list1
        curr2 = list2
            
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tmp = curr1.next
                newCurr.next = curr1
                curr1 = tmp
            else:
                tmp = curr2.next
                newCurr.next = curr2
                curr2 = tmp
            newCurr = newCurr.next

        if not curr1:
            newCurr.next = curr2
        elif not curr2:
            newCurr.next = curr1

        return newHead.next
