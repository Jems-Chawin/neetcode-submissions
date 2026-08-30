class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid_row = top + ((bottom - top) // 2)
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else: # target is in mid_row
                break 

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[mid_row][mid] > target:
                r = mid - 1
            elif matrix[mid_row][mid] < target:
                l = mid + 1
            else:
                return True
        return False
        