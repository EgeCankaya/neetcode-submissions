# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Phase 1: Find the exact midpoint
        # The fast pointer moves 2x faster compared to the slow one[cite: 17].
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Phase 2: Sever the connection and reverse the second half
        # You must sever the connection between the first half and the second half[cite: 25].
        second = slow.next
        prev = slow.next = None 
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # Phase 3: Weave the two independent lists together
        first, second = head, prev
        while second: # Loop simply runs until you hit None at the end of the reversed second list[cite: 30].
            # 1. Cache the futures into temporary variables [cite: 36]
            tmp1, tmp2 = first.next, second.next
            
            # 2. Rewire the current nodes [cite: 37]
            first.next = second
            second.next = tmp1
            
            # 3. Advance the pointers using the temporary variables [cite: 39]
            first, second = tmp1, tmp2