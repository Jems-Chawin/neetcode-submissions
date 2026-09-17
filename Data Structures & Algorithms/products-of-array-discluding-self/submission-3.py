class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst_return = [1] * (len(nums))
        lst_prefix = [1]
        lst_postfix = [1]

        for i in range(len(nums) - 1, -1, -1):
            lst_postfix.append(lst_postfix[-1] * nums[i])
        lst_postfix = lst_postfix[::-1]

        for i in range(len(nums)):
            lst_prefix.append(lst_prefix[-1] * nums[i])
            lst_return[i] = lst_prefix[i] * lst_postfix[i+1]
        
        return lst_return
