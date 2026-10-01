class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1_count = {}
        for char in s1:
            dict_s1_count[char] = 1 + dict_s1_count.get(char, 0)

        int_max_window_length = len(s1)
        dict_s2_count = {}
        l = 0
        while l + int_max_window_length <= len(s2):
            str_left_char = s2[l]
            dict_s2_count[str_left_char] = 1 + dict_s2_count.get(str_left_char, 0)
            for r in range(l + 1, l + int_max_window_length):
                str_cur_char = s2[r]
                dict_s2_count[str_cur_char] = 1 + dict_s2_count.get(str_cur_char, 0)
            if dict_s2_count == dict_s1_count:
                return True
            dict_s2_count = {}
            l += 1
        return False