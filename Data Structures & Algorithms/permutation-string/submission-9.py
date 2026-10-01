class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        int_max_window_length = len(s1)
        if int_max_window_length > len(s2):
            return False

        dict_s1_count = {}
        dict_s2_count = {}
        for i in range(int_max_window_length):
            str_cur_char_s1 = s1[i]
            str_cur_char_s2 = s2[i]
            dict_s1_count[str_cur_char_s1] = 1 + dict_s1_count.get(str_cur_char_s1, 0)
            dict_s2_count[str_cur_char_s2] = 1 + dict_s2_count.get(str_cur_char_s2, 0)
        if dict_s2_count == dict_s1_count:
            return True

        l = 1
        for r in range(l + int_max_window_length - 1, len(s2)):
            str_prev_left_char = s2[l-1]
            dict_s2_count[str_prev_left_char] -= 1
            if dict_s2_count[str_prev_left_char] <= 0:
                del dict_s2_count[str_prev_left_char]

            str_right_char = s2[r]
            dict_s2_count[str_right_char] = 1 + dict_s2_count.get(str_right_char, 0)
            if dict_s2_count == dict_s1_count:
                return True

            l += 1
        return False