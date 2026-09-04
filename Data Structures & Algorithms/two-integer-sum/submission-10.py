class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_checker = {}
        for i, n in enumerate(nums):
            int_prevVal = target - n
            if int_prevVal in dict_checker:
                return [dict_checker[int_prevVal], i]
            dict_checker[n] = i
        return -1