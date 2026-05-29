class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        maxC = 0

        for n in nums:
            cont = True
            c = 1
            curr = n
            while cont:
                if curr + 1 in nums:
                    c += 1
                    curr += 1
                else: 
                    cont = False
            maxC = max(maxC, c)

        return maxC