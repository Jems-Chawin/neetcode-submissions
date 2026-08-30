class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        to_return = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            to_return[tuple(counter)].append(s)
        return list(to_return.values())