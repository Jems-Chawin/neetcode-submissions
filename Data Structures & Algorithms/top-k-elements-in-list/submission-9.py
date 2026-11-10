class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_counter = {}
        # นับรายตัวเลข
        for int_n in nums:
            dict_counter[int_n] = dict_counter.get(int_n, 0) + 1

        list_temp = []
        # ใส่เข้า heap แบบ max มาก่อนด้วย -count
        for int_n, int_count in dict_counter.items():
            heapq.heappush(list_temp, (-int_count, int_n))
        
        list_return = []
        # pop ออกจาก heap เอาแค่ index
        for i in range(k):
            list_return.append(heapq.heappop(list_temp)[1])
        return list_return