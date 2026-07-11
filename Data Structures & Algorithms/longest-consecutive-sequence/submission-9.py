class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}

        for n in nums:
            hash_map[n] = 1
        maxC = 0
        
        for n in nums:
            cons = 0
            while n in hash_map:
                cons += 1 
                n += 1
                maxC = max(maxC, cons)
        return maxC
                 