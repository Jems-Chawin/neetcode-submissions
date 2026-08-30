class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = {}, {}
        def counting_func(counter_dict, target_string):
            for i in target_string:
                if i not in counter_dict:
                    counter_dict[i] = 1
                else:
                    counter_dict[i] += 1
            
        counting_func(s_counter, s)
        counting_func(t_counter, t)
        return s_counter == t_counter