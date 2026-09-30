class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_window = set()
        l = 0
        int_longest = 0

        for r in range(len(s)):
            str_end_window = s[r]
            while str_end_window in set_window:
                str_start_window = s[l]
                set_window.remove(str_start_window)
                l += 1
            set_window.add(str_end_window)
            int_longest = max(int_longest, len(set_window))
        return int_longest
            