# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Store sums in l1
        # Look for vals >= 10 in l1
        # add Node(1), store in l2
        cur, prev = l1, None
        while cur and l2:
            cur.val += l2.val
            prev, cur, l2 = cur, cur.next, l2.next
        if l2:
            prev.next = l2      # l1 ran out — splice l2's remaining nodes on

        cur = l1
        while cur:
            if cur.val >= 10:
                cur.val %= 10
                if cur.next:
                    cur.next.val += 1
                else:
                    cur.next = ListNode(1)
            cur = cur.next
        return l1
