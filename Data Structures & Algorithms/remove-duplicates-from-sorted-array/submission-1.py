class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # write_index tracks where we place the next unique number.
        # We start at 1 because the first element (index 0) is always unique.
        write_index = 1

        # Start scanning from the second element
        for i in range(1, len(nums)):
            # If current number is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index