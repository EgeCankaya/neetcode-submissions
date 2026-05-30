class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        #pair = [0, 0]
        diff = int(0)
        for x in range(len(nums)):
            map[nums[x]] = x    

        for x in range(len(nums)):
            diff = target - nums[x]
            if map.get(diff) != "None":
                return [x, map.get(target - nums[x])]

        