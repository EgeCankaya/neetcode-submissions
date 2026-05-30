class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = {}
        maj = []
        size = len(nums) / 3
        if len(nums) == 1:
            return [nums[0]]
            
        for x in nums:
            if x not in mp:
                mp[x] = 1
            else: 
                mp[x] += 1
                if mp[x] > size and x not in maj:
                    maj.append(x)
        return maj
        