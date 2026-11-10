class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_dict = {}
        # นับ occurence
        for n in nums:
            counter_dict[n] = counter_dict.get(n, 0) + 1

        heap_lst = []
        # ใช้ max heap เทคนิคด้วย -count
        for n, count in counter_dict.items():
            heapq.heappush(heap_lst, (-count, n))

        ret_lst = []
        for i in range(k):
            # pop เอาตัว n
            tmp = heapq.heappop(heap_lst)[1]
            ret_lst.append(tmp)
        return ret_lst