# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Start at the beginning of each list
        # Create a dummy node for the head
        # Compare both pointers
        # if l1 >= l2, point new list to l1 and continue

        l1, l2 = list1, list2
        dummy = ListNode(0)
        cur = dummy

        while (l1 and l2):
            if (l1.val <= l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 else l2 
        return dummy.next
            
