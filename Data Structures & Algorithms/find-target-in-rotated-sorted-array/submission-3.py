class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) //2
            if nums[m] == target:
                return m

            if nums[m] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m

            else:
                if nums[m] > target:
                    r = m + 1
                else:
                    l = m

        return -1
