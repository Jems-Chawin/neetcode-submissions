class Solution:
    def trap(self, height: List[int]) -> int:
        # === edge case ===
        if not height:
            return 0
        # =================
        l, r = 0, len(height) - 1
        max_hl_so_far, max_hr_so_far = height[l], height[r]
        ret_int = 0
        while l < r:
            # ไล่ดูว่าฝั่งที่เตี้ยกว่า
            if max_hl_so_far < max_hr_so_far:
                l += 1
                cur_hl = height[l]
                max_hl_so_far = max(max_hl_so_far, cur_hl)
                # ถ้าขยับซ้ายขึ้นแล้วมันเตี้ยกว่ามะกี้ ก็แปลว่ากักเก็บน้ำได้
                ret_int += max_hl_so_far - cur_hl
            else:
                r -= 1
                cur_hr = height[r]
                max_hr_so_far = max(max_hr_so_far, cur_hr)
                # ถ้าขยับขวาลงแล้วมันเตี้ยกว่ามะกี้ ก็แปลว่ากักเก็บน้ำได้
                ret_int += max_hr_so_far - cur_hr
        return ret_int