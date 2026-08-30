class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome_check = [i.lower() for i in s if i.isalnum()]
        l, r = 0, len(palindrome_check) - 1
        while l < r:
            if palindrome_check[l] != palindrome_check[r]:
                return False
            r -= 1
            l += 1
        return True