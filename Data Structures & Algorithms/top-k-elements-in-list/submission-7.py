class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_counter = {}
        for int_n in nums:
            if int_n not in dict_counter:
                dict_counter[int_n] = 1
            else:
                dict_counter[int_n] += 1

        list_temp = []
        for int_n, int_count in dict_counter.items():
            heapq.heappush(list_temp, (-int_count, int_n))
        
        list_return = []
        for i in range(k):
            list_return.append(heapq.heappop(list_temp)[1])
        return list_return