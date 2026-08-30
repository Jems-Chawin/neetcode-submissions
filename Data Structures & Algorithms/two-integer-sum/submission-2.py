class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''my attempt (time: O(n), space: O(n))'''
        # using hashmap
        seen = {}
        for i, n in enumerate(nums):
            # check first
            check = target - n
            if check in seen:
                return [seen[check], i]
            # then add in seen later
            seen[n] = i
        