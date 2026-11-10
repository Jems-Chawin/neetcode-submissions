class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # นับจำนวน occurence ของแต่ละ c in string
        def counting_func(input_str: str) -> dict:
            counter_dict = {}
            for c in input_str:
                counter_dict[c] = counter_dict.get(c, 0) + 1
            return counter_dict
        
        return counting_func(s) == counting_func(t)