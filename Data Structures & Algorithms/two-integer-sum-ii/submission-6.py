class Solution:
    def twoSum(self, lst_nums: List[int], target: int) -> List[int]:
        # l, r = 0, len(lst_nums) - 1
        # while l < r:
        #     int_sumVal = lst_nums[l] + lst_nums[r]
        #     if int_sumVal < target:
        #         l += 1
        #     elif int_sumVal > target:
        #         r -= 1
        #     else:
        #         return [l+1, r+1]

        dict_checker = {}
        for i, n in enumerate(lst_nums):
            int_check = target - n
            if int_check in dict_checker:
                return [dict_checker[int_check] + 1, i + 1]
            dict_checker[n] = i
        return -1
