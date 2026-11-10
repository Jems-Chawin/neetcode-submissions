class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret_lst = []
        nums_sorted_lst = sorted(nums)
        # ไล่จากตัวซ้ายสุดไป
        for i, left_n in enumerate(nums_sorted_lst):
            # === skip dups ===
            if left_n > 0:
                break
            if i > 0 and left_n == nums_sorted_lst[i-1]:
                continue
            # ==================
            l, r = i + 1, len(nums_sorted_lst) - 1
            while l < r:
                three_sum = left_n + nums_sorted_lst[l] + nums_sorted_lst[r]
                # เหมือนเดิม ผลรวมมากเกินไปก็ขยับขวาลง
                if three_sum > 0:
                    r -= 1
                # ผลรวมน้อยเกินไปก็ขยับซ้ายขึ้น
                elif three_sum < 0:
                    l += 1
                else:
                    ret_lst.append([left_n, nums_sorted_lst[l], nums_sorted_lst[r]])
                    l += 1
                    r -= 1
                    # === skip dups ===
                    while nums_sorted_lst[r] == nums_sorted_lst[r+1] and l < r:
                        r -= 1
                    while nums_sorted_lst[l] == nums_sorted_lst[l-1] and l < r:
                        l += 1
                    # =====================
        return ret_lst
        # overall ก็คล้ายๆ two sum 2 แต่มีการเอา left most n มาไล่คิดไปด้วย
                