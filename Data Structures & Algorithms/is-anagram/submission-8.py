class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = {}, {}
        for i in s:
            if i not in s_count:
                s_count[i] = 1
            else:
                s_count[i] += 1
        for i in t:
            if i not in t_count:
                t_count[i] = 1
            else:
                t_count[i] += 1
        return s_count == t_count