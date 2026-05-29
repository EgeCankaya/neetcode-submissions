class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        count = {}
        
        for x in range(r + 1):
                count[nums[x]] = 1 + count.get(nums[x], 0)
        
        maxV = max(count.keys())
        res.append(maxV)

        while r < len(nums) - 1:
            count[nums[l]] -= 1
            if  count[nums[l]] == 0:
                del count[nums[l]]
            r += 1
            l += 1
            count[nums[r]] = 1 + count.get(nums[r], 0)
            maxV = max(count.keys())
            res.append(maxV)
            

        return res