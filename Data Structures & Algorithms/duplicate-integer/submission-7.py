class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collect = set()
        for i in nums:
            if i in collect:
                return True
            collect.add(i)
        return False