class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keep_track = set()
        for i in nums:
            if i in keep_track:
                return True
            keep_track.add(i)
        return False