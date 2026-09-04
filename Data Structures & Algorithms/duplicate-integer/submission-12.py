class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_keepTrack = set()
        for i in nums:
            if i in set_keepTrack:
                return True
            set_keepTrack.add(i)
        return False