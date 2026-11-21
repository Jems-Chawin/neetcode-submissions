"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # tricky: 2 sorted list & 2 pointers
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        s, e = 0, 0
        ret_int = 0
        count = 0
        while s < len(intervals):
            # คือ ถ้า start ของ meeting ใหม่เริ่มก่อนโดยที่อันเดิมยังไม่ end ก็ต้องเปิดห้องประชุมใหม่เพิ่ม
            if starts[s] < ends[e]:
                s += 1
                count += 1
            # ส่วนอันนี้ก็ตรงกันข้าม
            else:
                e += 1
                count -= 1
            ret_int = max(count, ret_int)
        return ret_int