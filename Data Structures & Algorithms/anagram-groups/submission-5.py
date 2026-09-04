class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list_return = defaultdict(list)
        for s in strs:
            list_counter = [0] * 26
            for c in s:
                list_counter[ord(c) - ord("a")] += 1
            dict_list_return[tuple(list_counter)].append(s)
        return list(dict_list_return.values())