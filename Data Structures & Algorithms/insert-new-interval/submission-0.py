class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret_lst = []

        for i in range(len(intervals)):
            # Step 1: ดูตัว end time ของ newInterval ว่ามันอาจจะเร็วกว่าตัว interval start time ตัว interval ตัวปัจจุบัน ก็แปลว่าตัว newInterval เนี้ย มันมาก่อน
            if newInterval[1] < intervals[i][0]:
                ret_lst.append(newInterval)
                return ret_lst + intervals[i:]
            # Step 2: ดูตัว start time ของ newInterval ว่ามันมากกว่าตัว interval end time ของ ณ ตอนนี้ ก็คือถ้ามันมากกว่าก็แปลว่าไอ้ interval ตัวปัจจุบันจะต้องขึ้นก่อน
            elif newInterval[0] > intervals[i][1]:
                ret_lst.append(intervals[i])
            # Step 3: แล้วถ้ามันนอกเหนือจาก condition พวกนั้น มันก็แปลว่าตัว newInterval มันอาจจะเหลื่อมกับ interval ตัวปัจจุบันอยู่ ไม่ start time ก็ end time แต่ว่าเราก็เช็คได้โดยหา min และ max ไปเลย
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # ถ้ามันหลุดออกมาจากลูปเลยโดยไม่ return แปลว่า newInterval น่าจะเป็นตัวที่อยู่ท้ายสุด ก็ต้องอย่าลืม append มันเข้ามา
        ret_lst.append(newInterval)
        return ret_lst