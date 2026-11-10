class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_int = 0
        for n in nums:
            # คุณเป็นหัวแถวรึเปล่า?
            if n - 1 not in nums_set:
                length_int = 1
                # คุณได้เป็นหัวแถวละ แต่แถวคุณยาวแค่ไหน?
                while n + length_int in nums_set:
                    length_int += 1
                longest_int = max(longest_int, length_int)
        return longest_int