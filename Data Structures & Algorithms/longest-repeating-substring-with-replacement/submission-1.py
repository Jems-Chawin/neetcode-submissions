class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter_dict = {}
        ret_int = 0
        l = 0
        # step 1: expand window ไปเรื่อยๆ แล้วเก็บค่า longest ไว้
        for r in range(len(s)):
            end_window_str = s[r]
            counter_dict[end_window_str] = counter_dict.get(end_window_str, 0) + 1
            # step 2: ถ้า window size เกินกว่า max count ของตัวซ้ำ มากกว่า k ตัวแล้ว ก็ถึงเวลาต้อง shrink window แล้ว
            while (r - l + 1) - max(counter_dict.values()) > k:
                start_window_str = s[l]
                counter_dict[start_window_str] -= 1
                l += 1
            ret_int = max(ret_int, r - l + 1)
        return ret_int