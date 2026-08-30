class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_parentheses = { ")" : "(", "]" : "[", "}" : "{" }

        for each in s:
            if each in map_parentheses:
                if stack and stack[-1] == map_parentheses[each]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(each)
        return stack == []