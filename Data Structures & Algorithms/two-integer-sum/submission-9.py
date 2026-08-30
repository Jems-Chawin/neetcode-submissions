class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker_dict = {}
        for i, n in enumerate(nums):
            prev_value = target - n
            if prev_value in checker_dict:
                return [checker_dict[prev_value], i]
            checker_dict[n] = i
        return -1