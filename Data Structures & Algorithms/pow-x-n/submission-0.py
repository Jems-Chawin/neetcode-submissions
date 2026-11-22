class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            ret = helper(x, n // 2)
            ret = ret * ret
            return x * ret if n % 2 else ret

        out = helper(x, abs(n))
        return out if n >= 0 else 1 / out