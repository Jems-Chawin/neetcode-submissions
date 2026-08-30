class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        for n in nums:
            if n not in counter_dict:
                counter_dict[n] = 1
            else:
                counter_dict[n] += 1

        temp = []
        for n, count in counter_dict.items():
            heapq.heappush(temp, (-count, n))
        
        to_return = []
        for i in range(k):
            to_return.append(heapq.heappop(temp)[1])
        return to_return