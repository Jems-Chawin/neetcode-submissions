class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_rows = defaultdict(set)
        dict_cols = defaultdict(set)
        dict_grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                str_curVal = board[r][c]
                if str_curVal == ".":
                    continue
                if (str_curVal in dict_rows[r] or 
                str_curVal in dict_cols[c] or 
                str_curVal in dict_grid[(r//3, c//3)]):
                    return False
                dict_rows[r].add(str_curVal)
                dict_cols[c].add(str_curVal)
                dict_grid[(r//3, c//3)].add(str_curVal)
        return True