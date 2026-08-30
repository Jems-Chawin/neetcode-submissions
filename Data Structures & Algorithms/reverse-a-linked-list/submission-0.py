# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def flip_pointer(node_left, node_mid, node_right):
            node_mid.next = node_left
            if node_right == None: # This means it is at the end of list
                return node_mid
            return flip_pointer(node_mid, node_right, node_right.next)

        prev_node = None
        cur_node = head
        if cur_node == None:
            return cur_node
        next_node = cur_node.next

        return flip_pointer(prev_node, cur_node, next_node)