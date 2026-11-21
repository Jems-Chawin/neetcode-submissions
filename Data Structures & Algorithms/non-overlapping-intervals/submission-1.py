class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        ret_int = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            # Step 1: ถ้ามัน overlap ก็ ret + 1 และ update prev_end ให้เน้นไปที่ตัวที่จะกระเถิบน้อยสุด เพราะเราจะเน้น minimum "greedy approach, avoid later potentials overlapping"
            if interval[0] < prev_end:
                ret_int += 1
                prev_end = min(interval[1], prev_end)
            # Step 2: ถ้าไม่ overlap ก็แค่ update prev_end เป็นของตัว interval ถัดไป
            else:
                prev_end = interval[1]
        return ret_int