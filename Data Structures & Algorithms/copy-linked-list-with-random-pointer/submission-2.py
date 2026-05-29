
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Dictionary to map original nodes to their cloned counterparts
        old_to_new = {}
        
        # First Pass: Create all the isolated clone nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Second Pass: Wire the .next and .random pointers
        curr = head
        while curr:
            clone = old_to_new[curr]
            
            # Use .get() to safely handle None values (e.g., the tail's .next)
            clone.next = old_to_new.get(curr.next)
            clone.random = old_to_new.get(curr.random)
            
            curr = curr.next
            
        # Return the head of the newly cloned list
        return old_to_new[head]