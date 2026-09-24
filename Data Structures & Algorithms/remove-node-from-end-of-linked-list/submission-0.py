# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count how long the list is,
        # create dummy node for edge cases
        # loop to len-(n+1) including the dummy
        # connect the node before to the one being removed.next

        cur = head
        length = 1
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(length - (n+1)):
            cur = cur.next
        cur.next = cur.next.next

        return dummy.next