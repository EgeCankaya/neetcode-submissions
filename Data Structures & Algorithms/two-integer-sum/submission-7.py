class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh_map = {}

        for x in range(len(nums)):
            diff = target - nums[x]

            if diff in hsh_map:
                return [hsh_map[diff], x]
            else:
                hsh_map[x] = nums[x]