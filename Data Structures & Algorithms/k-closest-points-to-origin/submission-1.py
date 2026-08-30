class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for p in points:
            dist = -(p[0]*p[0] + p[1]*p[1])
            if len(max_heap) >= k:
                heapq.heappush(max_heap, (dist, p))
                heapq.heappop(max_heap)
            else:
                heapq.heappush(max_heap, (dist, p))
        return [p for _, p in max_heap]