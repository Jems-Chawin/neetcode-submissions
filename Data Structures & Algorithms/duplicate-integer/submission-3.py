class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using hashset to keep the "already seen" number
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False