class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # concept: search lower bound
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        # pivot is the starting point of the right half of sorted array
        pivot = l
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]: # target might be in right half?
            l = pivot
        else: # or left half?
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1
        