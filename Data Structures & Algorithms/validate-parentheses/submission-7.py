class Solution:
    def isValid(self, s: str) -> bool:
        lst_stack_open = []
        dict_bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            # ถ้าเป็นเปิดให้เก็บลง stack
            if bracket in dict_bracket_pairs:
                lst_stack_open.append(bracket)
            # ถ้าปิดโผล่มา
            else:
                # ต้องดูก่อนว่ามีเปิดมาก่อนหน้านั้นไหม แล้วก็ check ตัวบนสุด ว่าเข้าคู่ไหม
                if lst_stack_open:
                    if bracket != dict_bracket_pairs[lst_stack_open[-1]]:
                        return False
                    lst_stack_open.pop()
                # ถ้าไม่มีก็จบเลย
                else:
                    return False
        return lst_stack_open == []