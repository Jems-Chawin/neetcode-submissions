class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_rows = defaultdict(set)
        dict_cols = defaultdict(set)
        dict_grid = defaultdict(set)

        for row in range(9):
            for col in range(9):
                str_curVal = board[row][col]
                if str_curVal == ".":
                    continue
                if (str_curVal in dict_rows[row] or 
                str_curVal in dict_cols[col] or 
                str_curVal in dict_grid[(row//3, col//3)]):
                    return False
                dict_rows[row].add(str_curVal)
                dict_cols[col].add(str_curVal)
                dict_grid[(row//3, col//3)].add(str_curVal)
        return True