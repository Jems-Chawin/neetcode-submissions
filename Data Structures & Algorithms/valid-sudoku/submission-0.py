class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur_val = board[r][c]
                if cur_val == ".":
                    continue
                if (cur_val in rows[r]
                    or cur_val in cols[c]
                    or cur_val in grid[(r // 3, c // 3)]):
                    return False
                rows[r].add(cur_val)
                cols[c].add(cur_val)
                grid[(r // 3, c // 3)].add(cur_val)
        return True