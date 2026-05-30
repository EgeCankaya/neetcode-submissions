class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = {}
        max_consec = 0
        consecutive = 0
        consec = True

        for i in range(len(nums)):
            arr[nums[i]] = i
        
        for x in range(len(nums)):
            y = x
            while consec:
                if arr.get(nums[y] + 1) is not None:
                    consecutive += 1
                    y = arr.get(nums[y] + 1)
                else:
                    consec = False
                    if consecutive > max_consec:
                        max_consec = consecutive       
            consec = 0

            
        return consecutive + 1

