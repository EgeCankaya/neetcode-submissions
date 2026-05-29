class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = defaultdict(list)

        for i, num in enumerate(nums):
            index_map[num].append(i)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in index_map:
                for j in index_map[diff]:
                    if i != j:
                        return [i, j]
