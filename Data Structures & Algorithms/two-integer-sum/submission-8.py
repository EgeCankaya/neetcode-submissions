class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_map = {}

        for i, x in enumerate(nums):
            diff = target - x

            if diff in hsh_map:
                return [hsh_map[diff], i]
            else:
                hsh_map[i] = x