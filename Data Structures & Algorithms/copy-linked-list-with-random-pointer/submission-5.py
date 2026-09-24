"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Two pass approach
        # first pass, create corresponding new node for each node in old list
        # map each old node to new node using a hashmap
        # In second pass
        # assign next and random values to the value of key in hashmap

        if not head:
            return None
        
        hashmap = { None : None}
        # first pass
        cur = head
        while cur:
            node = Node(cur.val)
            hashmap[cur] = node
            cur = cur.next
        
        # second pass
        new_head = hashmap[head]
        cur = head
        cur1 = new_head

        while cur:
            cur1.next = hashmap[cur.next]
            cur1.random = hashmap[cur.random]
            cur1 = cur1.next
            cur = cur.next
        
        return new_head

            