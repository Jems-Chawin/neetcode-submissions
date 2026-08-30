class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        srt_lst = sorted(lst)
        n = len(srt_lst)
        if n % 2 == 0:
            return (srt_lst[n//2 - 1] + srt_lst[n//2]) / 2
        return srt_lst[n//2]