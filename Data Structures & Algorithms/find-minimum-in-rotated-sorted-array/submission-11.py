class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r) //2
            if l < m:
                l = m
            else:
                r = m
        
        return nums[l]