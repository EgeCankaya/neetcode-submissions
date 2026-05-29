class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = {}
        max_consec = 0
        consecutive = 0

        for i in range(len(nums)):
            arr[nums[i]] = i
        
        for x in range(len(nums)):
            y = x
            consec = True
            while consec:
                if arr.get(nums[y] + 1) is not None:
                    consecutive += 1
                    y = arr.get(nums[y] + 1)
                else:
                    consec = False
                    if consecutive > max_consec:
                        max_consec = consecutive       
            consecutive = 0

            
        return 0 if not nums else max_consec + 1


