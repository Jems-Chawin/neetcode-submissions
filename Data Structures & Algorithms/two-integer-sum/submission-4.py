class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in collect:
                return [collect[check], i]
            collect[n] = i