class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pool_set = set()
        ret_int = 0
        l = 0

        # step 1: loop เก็บเข้า pool
        for r in range(len(s)):
            end_window_str = s[r]
            # step 2: ต้องตัดหัว window ส่วน sub-string เก่าออกให้หมด
            while end_window_str in pool_set:
                start_window_str = s[l]
                pool_set.remove(start_window_str)
                l += 1
            pool_set.add(end_window_str)
            ret_int = max(ret_int, len(pool_set))

        return ret_int
            