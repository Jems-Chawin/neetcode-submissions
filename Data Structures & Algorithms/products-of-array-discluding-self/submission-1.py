class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_return = [1] * (len(nums))
        int_prefix = 1
        int_postfix = 1

        for i in range(len(nums)):
            list_return[i] = int_prefix
            int_prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            list_return[i] *= int_postfix
            int_postfix *= nums[i]
        
        return list_return