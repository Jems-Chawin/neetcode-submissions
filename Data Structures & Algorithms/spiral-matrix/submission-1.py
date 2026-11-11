class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret_lst = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        while l < r and t < b:
            # step 1: first row, left to right
            for i in range(l, r):
                ret_lst.append(matrix[t][i])
            t += 1
            # step 2: last col, top to bottom
            for i in range(t, b):
                ret_lst.append(matrix[i][r - 1])
            r -= 1
            # check if it's already done
            if len(ret_lst) == (len(matrix) * len(matrix[0])):
                break
            # step 3: last row, right to left
            for i in range(r - 1, l - 1, -1):
                ret_lst.append(matrix[b - 1][i])
            b -= 1
            # step 4: first col, bottom to top
            for i in range(b - 1, t - 1, -1):
                ret_lst.append(matrix[i][l])
            l += 1
        return ret_lst
