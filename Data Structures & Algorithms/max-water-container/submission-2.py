class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        water = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            water = max(water, area)

            if heights[left + 1] > heights[right - 1]:
                left += 1
            else:
                right -= 1
        
        return water