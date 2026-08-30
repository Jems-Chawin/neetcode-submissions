class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        output = [1] * array_length
        i = 0
        probe = 0
        while probe <= array_length:
            if probe == i:
                probe += 1
                continue
            if probe == array_length and i < array_length:
                probe = 0
                i += 1
                if i == array_length:
                    break
            output[i] *= nums[probe]
            probe += 1
        return output

