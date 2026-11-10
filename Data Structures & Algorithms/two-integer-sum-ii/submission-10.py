class Solution:
    def twoSum(self, lst_nums: List[int], target: int) -> List[int]:
        l, r = 0, len(lst_nums) - 1
        while l < r:
            sum_int = lst_nums[l] + lst_nums[r]
            # มากไปให้เขยิบขวาลง
            if sum_int > target:
                r -= 1
            # น้อยไปให้เขยิบซ้ายขึ้น
            elif sum_int < target:
                l += 1
            else:
                return [l+1, r+1]
        return -1
