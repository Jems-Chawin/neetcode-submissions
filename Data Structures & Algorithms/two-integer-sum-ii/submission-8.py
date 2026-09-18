class Solution:
    def twoSum(self, lst_nums: List[int], target: int) -> List[int]:
        l, r = 0, len(lst_nums) - 1
        while l < r:
            int_sumVal = lst_nums[l] + lst_nums[r]
            if int_sumVal < target:
                l += 1
            elif int_sumVal > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []
