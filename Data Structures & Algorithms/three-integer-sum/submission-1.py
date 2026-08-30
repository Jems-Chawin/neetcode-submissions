class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''my attempt (time: O(n^2))'''
        nums.sort() # O(nlogn)
        output = []
        # main algorithm O(n^2)
        for i, n in enumerate(nums):
            # redundant elements
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                sum_val = n + nums[l] + nums[r]
                if sum_val > 0:
                    r -= 1
                elif sum_val < 0:
                    l += 1
                else:
                    output.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # redundant elements
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return output