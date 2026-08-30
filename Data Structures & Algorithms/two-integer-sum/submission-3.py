class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in seen:
                return [seen[check], i]
            seen[n] = i