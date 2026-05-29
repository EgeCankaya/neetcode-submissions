class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for x in nums:
            if x in hash_map:
                return True
            else:
                hash_map[x] = -1
        return False