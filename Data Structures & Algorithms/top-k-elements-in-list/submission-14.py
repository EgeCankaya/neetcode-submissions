class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [[] for i in range(len(nums) + 1)]
        mp = {}
        for x in nums:
            mp[x] = 1 + mp.get(x, 0)
        for num, count in mp.items():
            res[count].append(num)
        kfreq = []
        for x in range(len(res) - 1, 0, -1):
            for num in res[x]:
                kfreq.append(num)
                if len(kfreq) == k:
                    return kfreq

