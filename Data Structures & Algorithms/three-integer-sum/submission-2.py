class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst_return = []
        lst_sortedNums = sorted(nums)

        for i, int_leftMostVal in enumerate(lst_sortedNums):
            if int_leftMostVal > 0:
                break
            
            if i > 0 and int_leftMostVal == lst_sortedNums[i - 1]:
                continue

            l, r = i + 1, len(lst_sortedNums) - 1
            while l < r:
                int_threeSum = int_leftMostVal + lst_sortedNums[l] + lst_sortedNums[r]
                if int_threeSum > 0:
                    r -= 1
                elif int_threeSum < 0:
                    l += 1
                else:
                    lst_return.append([int_leftMostVal, lst_sortedNums[l], lst_sortedNums[r]])
                    l += 1
                    r -= 1
                    while lst_sortedNums[l] == lst_sortedNums[l - 1] and l < r:
                        l += 1
                    while lst_sortedNums[r] == lst_sortedNums[r + 1] and l < r:
                        r -= 1
        return lst_return
                