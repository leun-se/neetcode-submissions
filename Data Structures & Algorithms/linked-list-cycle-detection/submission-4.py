# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a slow and fast pointer
        # return False if fast pointer is None
        # return True if fast pointer == slow pointer
        if (not head):
            return False

        pt = head
        while(pt and pt.next):
            head = head.next

            pt = pt.next.next

            if (head == pt):
                return True
        return False
