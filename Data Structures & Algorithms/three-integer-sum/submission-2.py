class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        res = []
        n = len(nums)

        for curr in range(n):
            l, r = curr + 1, n - 1
            if nums[curr] not in seen:
                seen.add(nums[curr])
            else:
                continue

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

        return res                    
                                

