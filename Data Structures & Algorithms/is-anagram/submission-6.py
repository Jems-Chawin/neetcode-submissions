class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''my attempt (time: O(1*2*n), space: O(2*k))'''
        # edge case
        if len(s) != len(t):
            return False

        # main algorithm
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        # can just use return count_s == count_t
        for i in count_s:
            if count_s[i] != count_t.get(i, 0):
                return False
        return True
        