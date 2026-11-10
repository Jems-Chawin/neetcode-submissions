class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lst = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(s_lst) - 1
        # ไล่ check จากทั้งซ้ายและขวา
        while l < r:
            if s_lst[l] != s_lst[r]:
                return False
            l += 1
            r -= 1
        return True