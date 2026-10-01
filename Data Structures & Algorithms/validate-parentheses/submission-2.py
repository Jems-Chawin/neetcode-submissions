class Solution:
    def isValid(self, s: str) -> bool:
        lst_stack = []
        dict_bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        for bracket in s:
            if bracket in dict_bracket_pairs:
                lst_stack.append(bracket)
            elif lst_stack and bracket == dict_bracket_pairs[lst_stack[-1]]:
                lst_stack.pop()
            else:
                return False
        return lst_stack == []