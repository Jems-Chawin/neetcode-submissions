class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        zeroes_row = [False] * n_rows
        zeroes_col = [False] * n_cols
        # step 1: ไล่ดูว่า row/col ไหนบ้างที่จะต้องเป็น 0
        for r in range(n_rows):
            for c in range(n_cols):
                if matrix[r][c] == 0:
                    zeroes_row[r] = True
                    zeroes_col[c] = True
        
        # step 2: ไล่ update row/col นั้นๆให้เป็น 0
        for r in range(n_rows):
            for c in range(n_cols):
                if zeroes_row[r] or zeroes_col[c]:
                    matrix[r][c] = 0