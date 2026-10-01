class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_counter = {}
        int_return = 0
        l = 0

        for r in range(len(s)):
            str_end_window = s[r]
            dict_counter[str_end_window] = 1 + dict_counter.get(str_end_window, 0)

            while (r - l + 1) - max(dict_counter.values()) > k:
                str_start_window = s[l]
                dict_counter[str_start_window] -= 1
                l += 1

            int_return = max(int_return, r - l + 1)

        return int_return