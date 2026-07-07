class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for i in range(len(points)):
            d = [(points[i][0] ** 2) + (points[i][1] ** 2), i]
            heapq.heappush(dist, d)

        res = []
        while k > 0:
            i = heapq.heappop(dist)
            i = i[1]
            res.append(points[i])
            k -= 1
        
        return res
