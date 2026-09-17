class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst_checkPalindrome = [i.lower() for i in s if i.isalnum()]
        l, r = 0, len(lst_checkPalindrome) - 1
        while l < r:
            if lst_checkPalindrome[l] != lst_checkPalindrome[r]:
                return False
            l += 1
            r -= 1
        return True