class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] in unique:
                nums.pop(i)
                i -= 1
                size -= 1
            else:
                unique.add(nums[i])
            i += 1
        return len(unique)
        
        