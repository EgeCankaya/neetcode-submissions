# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = 1
        while curr:
            if curr.next == None:
                curr.next = head
            elif c == n:
                curr.next = curr.next.next
                return head
            else:
                curr = curr.next
            c += 1

        if head == None:
            return []
            
        


        