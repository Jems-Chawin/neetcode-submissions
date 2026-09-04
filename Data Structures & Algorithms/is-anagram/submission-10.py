class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_sCounter, dict_tCounter = {}, {}
        def counting_func(dict_counter, str_target):
            for c in str_target:
                if c not in dict_counter:
                    dict_counter[c] = 1
                else:
                    dict_counter[c] += 1
            
        counting_func(dict_sCounter, s)
        counting_func(dict_tCounter, t)
        return dict_sCounter == dict_tCounter