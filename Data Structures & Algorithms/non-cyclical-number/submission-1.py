class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n: int) -> int:
            output = 0
            while n:
                digit = n % 10
                output += digit * digit
                n = n // 10
            return output

        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = sumOfSquares(n)
        return False
