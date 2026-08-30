class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            temp = []
            for _ in range(2):
                curr_largest_stone = -heapq.heappop(max_heap)
                temp.append(curr_largest_stone)
            if temp[0] == temp[1]:
                continue
            else:
                heapq.heappush(max_heap, -(temp[0] - temp[1]))
        return -max_heap[0] if max_heap else 0