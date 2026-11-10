class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_lst = [1] * len(nums)
        postfix_lst = [1]
        prefix_lst = [1]

        # ไล่เก็บ postfix
        for i in range(len(nums) - 1, -1, -1):
            tmp = postfix_lst[-1] * nums[i]
            postfix_lst.append(tmp)
        postfix_lst = postfix_lst[::-1]

        # ไล่เก็บ prefix + คูณตัวหน้าและตัวหลังไปด้วยเลย
        for i in range(len(nums)):
            tmp = prefix_lst[-1] * nums[i]
            prefix_lst.append(tmp)
            ret_lst[i] = prefix_lst[i] * postfix_lst[i+1]

        return ret_lst
