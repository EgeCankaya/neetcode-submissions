class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            # Take a snapshot of how many nodes are on this current level
            level_size = len(queue)
            
            # Process strictly the nodes on this level
            for _ in range(level_size):
                curr = queue.popleft() # FIFO: Pop from the front!
                
                # Add the next level's children to the back of the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            # Once the 'for' loop finishes, we have fully processed one level
            depth += 1
            
        return depth