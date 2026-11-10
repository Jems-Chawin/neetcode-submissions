class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker_set = set()
        # ให้ยามยืน check ว่าใครมาเข้าซ้ำ
        for i in nums:
            if i in tracker_set:
                return True
            tracker_set.add(i)
        return False