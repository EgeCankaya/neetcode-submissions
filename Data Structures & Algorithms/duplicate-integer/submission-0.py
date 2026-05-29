class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = bool(False)
        map = {"x":"x"}
        
        for x in nums:
            if map.get(x) == "Exists":
                return True
            else:
                map[x] = "Exists"
        
        return dupe
        
        