class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict = defaultdict(set)
        cols_dict = defaultdict(set)
        grid_dict = defaultdict(set)

        # มันคือ contain duplicate แต่มาใช้กับ matrix sudoku
        for r in range(9):
            for c in range(9):
                cur_str = board[r][c]
                if cur_str == ".":
                    continue
                if (cur_str in rows_dict[r]) or (cur_str in cols_dict[c]) or (cur_str in grid_dict[(r//3,c//3)]):
                    return False
                rows_dict[r].add(cur_str)
                cols_dict[c].add(cur_str)
                # มอง grid ให้ zoomed out เป็น 3x3 ได้
                grid_dict[(r//3,c//3)].add(cur_str)
        return True