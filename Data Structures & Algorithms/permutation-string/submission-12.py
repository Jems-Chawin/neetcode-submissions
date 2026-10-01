class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # ดัก edge case ที่ obviously false
        int_max_window_length = len(s1)
        if int_max_window_length > len(s2):
            return False

        lst_s1_count = [0] * 26
        lst_s2_count = [0] * 26
        # check n ตัวแรกที่เป็น len(s1) ก่อนเลย
        for i in range(int_max_window_length):
            str_cur_char_s1 = s1[i]
            lst_s1_count[ord(str_cur_char_s1) - ord("a")] += 1
            str_cur_char_s2 = s2[i]
            lst_s2_count[ord(str_cur_char_s2) - ord("a")] += 1
        if lst_s2_count == lst_s1_count:
            return True

        l = 1
        for r in range(l + int_max_window_length - 1, len(s2)):
            str_prev_left_char = s2[l-1]
            lst_s2_count[ord(str_prev_left_char) - ord("a")] -= 1
            str_right_char = s2[r]
            lst_s2_count[ord(str_right_char) - ord("a")] += 1

            if lst_s2_count == lst_s1_count:
                return True

            l += 1

        return False