class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for n in nums:
            if hash_map.get(n) == 1:
                return True
            else:
                hash_map[n] = 1
        return False