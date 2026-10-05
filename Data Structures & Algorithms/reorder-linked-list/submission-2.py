# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        prevMap = {}
        prev = None
        currEnd = head
        while currEnd:
            prevMap[currEnd] = prev
            prev = currEnd
            currEnd = currEnd.next

        currEnd = prev 
        curr = head
        i = 0
        while curr and curr.next != currEnd:
            # self.printList(head)
            if i % 2 == 0:
                # Even, take from end
                tmp = curr.next
                curr.next = currEnd
                currEnd.next = tmp
                currEnd = prevMap[currEnd]
                currEnd.next = None
            # Odd, do nothing
            curr = curr.next
            i += 1 

    def printList(self, head):
        s = ""
        curr = head
        while curr != None:
            s += f"{curr.val} ->"
            curr = curr.next
        print(s)