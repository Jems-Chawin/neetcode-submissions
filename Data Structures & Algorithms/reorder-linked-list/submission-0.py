# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find the middle part of list in order to cut in half
        # using the slow and fast technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse the second half
        head2 = slow.next
        slow.next = None
        prev = None
        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp
        
        # Step 3: re-point each head of the 2 lists
        head1, head2 = head, prev
        while head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2
        