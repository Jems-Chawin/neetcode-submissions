class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_checker = set()
        l = 0
        int_longest = 0

        # dynamic เพิ่มลด window ได้
        for r in range(len(s)):
            str_end_window = s[r]
            # ต้องตัดหัว window ส่วน sub-string เก่าออกให้หมด
            while str_end_window in set_checker:
                str_start_window = s[l]
                set_checker.remove(str_start_window)
                l += 1
            set_checker.add(str_end_window)
            int_longest = max(int_longest, len(set_checker))

        return int_longest
            