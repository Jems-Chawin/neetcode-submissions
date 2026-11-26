# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Step 1: move right pointer to the left + n position
        while n > 0:
            right = right.next
            n -= 1
        
        # Step 2: move 2 pointers along together until the end
        while right:
            left = left.next
            right = right.next

        # Step 3: remove that specific node by just skip pass it
        left.next = left.next.next
        return dummy.next # <- head node all along