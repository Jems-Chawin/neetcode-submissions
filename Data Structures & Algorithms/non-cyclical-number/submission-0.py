class Solution:
    def isHappy(self, n: int) -> bool:
        store = 0
        seen = set()
        while True:
            digit = n % 10
            store += digit * digit
            n = n // 10
            if n == 0:
                if store == 1:
                    return True
                if store in seen:
                    return False
                seen.add(store)
                n = store
                store = 0
