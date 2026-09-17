class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        int_longest = 0
        for i in nums:
            if i - 1 not in set_nums:
                int_length = 1
                while i + int_length in set_nums:
                    int_length += 1
                int_longest = max(int_longest, int_length)
        return int_longest
                