class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dict_s1_count = {}
        for char in s1:
            dict_s1_count[char] = 1 + dict_s1_count.get(char, 0)

        int_max_window_length = len(s1)
        dict_s2_count = {}
        for i in range(int_max_window_length):
            str_cur_char = s2[i]
            dict_s2_count[str_cur_char] = 1 + dict_s2_count.get(str_cur_char, 0)
        if dict_s2_count == dict_s1_count:
            return True

        l = 1
        r = l + int_max_window_length - 1
        while r < len(s2):
            str_prev_left_char = s2[l-1]
            dict_s2_count[str_prev_left_char] -= 1
            if dict_s2_count[str_prev_left_char] <= 0:
                del dict_s2_count[str_prev_left_char]

            str_right_char = s2[r]
            dict_s2_count[str_right_char] = 1 + dict_s2_count.get(str_right_char, 0)
            if dict_s2_count == dict_s1_count:
                return True
                
            r += 1
            l += 1
        return False