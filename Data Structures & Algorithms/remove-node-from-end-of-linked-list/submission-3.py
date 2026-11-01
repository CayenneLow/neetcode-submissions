# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(val=0, next=head)

        curr = dummyNode
        front = dummyNode
        while n > 0:
            front = front.next
            n -= 1

        while front.next:
            curr = curr.next
            front = front.next

        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return dummyNode.next