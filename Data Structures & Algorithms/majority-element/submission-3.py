class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = {}
        for x in nums:
            if x not in maj:
                maj[x] = 1
            else:
                maj[x] += 1
                if maj[x] > len(nums) / 2 or len(nums) == 1:
                    return x
        