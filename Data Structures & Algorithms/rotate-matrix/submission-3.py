class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # step 1: transpose matrix
        for row in range(len(matrix)):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # step 2: reverse row
        for row in matrix:
            row.reverse()