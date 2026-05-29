class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # stores *indices*, not values

        for i in range(len(nums)):
            # 1. Remove elements that are no longer in the current window
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. Remove elements from the right that are smaller than the current element
            # They can NEVER be the maximum in this or any future window
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # 3. Add the current element's index
            q.append(i)
            
            # 4. If our window has reached size k, add the max (at the front of deque) to results
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res