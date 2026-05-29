class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for curr in range(n):
            # O(1) Space Optimization: Skip duplicates for the outer pointer 
            # without needing the 'seen' set
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            l, r = curr + 1, n - 1

            while l < r:
                sums = nums[l] + nums[r] 
                target = -1 * nums[curr]
                
                if sums > target:
                    r -= 1
                elif sums < target:
                    l += 1
                else:
                    res.append([nums[curr], nums[l], nums[r]])
                    l += 1
                    r -= 1
                
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res