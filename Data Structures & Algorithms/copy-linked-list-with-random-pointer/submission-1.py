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
        hashmap = {None: None}

        # Step 1: keep a copy of the old nodes
        old = head
        while old:
            copy = Node(old.val)
            hashmap[old] = copy
            old = old.next
        
        # Step 2: construct a new nodes from it
        new = head
        while new:
            copy = hashmap[new]
            copy.next = hashmap[new.next]
            copy.random = hashmap[new.random]
            new = new.next

        return hashmap[head]