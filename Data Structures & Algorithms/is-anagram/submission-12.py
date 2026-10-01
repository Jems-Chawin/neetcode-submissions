class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict_sCounter, dict_tCounter = {}, {}
        # นับจำนวน occurence รายตัวอักษร
        for i in range(len(s)):
            dict_sCounter[s[i]] = 1 + dict_sCounter.get(s[i], 0)
            dict_tCounter[t[i]] = 1 + dict_tCounter.get(t[i], 0)
            
        return dict_sCounter == dict_tCounter