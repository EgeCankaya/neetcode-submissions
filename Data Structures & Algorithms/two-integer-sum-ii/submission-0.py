class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                # Convert to 1-indexed
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
        