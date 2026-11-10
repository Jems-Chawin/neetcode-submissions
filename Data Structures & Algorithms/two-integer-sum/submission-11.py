class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect_dict = {}
        for i, n in enumerate(nums):
            # ยาม check ว่าเคยมีตัวก่อนหน้าเข้ามารึยัง
            prev_n = target - n
            if prev_n in collect_dict:
                return [collect_dict[prev_n], i]
            collect_dict[n] = i
        return -1