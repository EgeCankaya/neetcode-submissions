class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_map = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]

            if diff in hsh_map:
                return [hsh_map[diff], i]
            else:
                hsh_map[nums[i]] = i
