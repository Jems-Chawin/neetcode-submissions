class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort เพื่อให้สามารถไล่ดูไปทีละตัวได้ง่ายๆ
        intervals.sort(key=lambda x: x[0])
        ret_lst = [intervals[0]]
        for interval in intervals[1:]:
            # start time ของตัวขวา overlap กับ interval ตัวซ้ายก็ต้องทำการ merge
            if interval[0] <= ret_lst[-1][1]:
                ret_lst[-1][1] = max(interval[1], ret_lst[-1][1])
            # ถ้าไม่ก็ append ไปต่อ
            else:
                ret_lst.append(interval)
        return ret_lst