class Solution:
    def isValid(self, s: str) -> bool:
        lst_stack = []
        dict_bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            # ถ้าเป็นเปิดให้เก็บลง stack
            if bracket in dict_bracket_pairs:
                lst_stack.append(bracket)
            # ถ้าปิดโผล่มา ต้องดูก่อนว่ามีเปิดมาก่อนหน้านั้นไหม แล้วก็ check ตัวบนสุด ว่าเข้าคู่ไหม
            elif lst_stack:
                if bracket != dict_bracket_pairs[lst_stack[-1]]:
                    return False
                lst_stack.pop()
            else:
                return False
        return lst_stack == []