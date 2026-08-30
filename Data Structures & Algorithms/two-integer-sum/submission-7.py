class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in seen:
                return [seen[check], i]
            elif n not in seen:
                seen[n] = i
        return -1