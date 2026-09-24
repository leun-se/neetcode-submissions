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

        fp, sp = head, head
        while(sp and fp):
            sp = sp.next
            fp = fp.next
            if (not fp):
                return False
            fp = fp.next
            if (sp == fp):
                return True
        return False
