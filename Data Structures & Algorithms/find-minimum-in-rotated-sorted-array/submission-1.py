class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # We use left < right instead of left <= right because we are 
        # converging on a single element (the minimum) rather than 
        # searching for a specific target value.
        while left < right:
            # Calculate mid to prevent integer overflow (more relevant in C++/Java)
            mid = left + (right - left) // 2

            # Scenario A: The right half is perfectly sorted. 
            # The cliff (minimum) must be at 'mid' or to the left of it.
            if nums[mid] < nums[right]:
                right = mid  # We keep 'mid' because it might be the minimum itself

            # Scenario B: The middle value is greater than the right value.
            # Monotonicity is broken, so the cliff is strictly to the right of 'mid'.
            else:
                left = mid + 1 # 'mid' is definitely NOT the minimum, so we skip it

        # When the loop breaks, left == right, meaning our pointers have trapped the minimum.
        return nums[left]