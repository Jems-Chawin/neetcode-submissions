class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''my attempt (time: O(n^2*k), space: O(n*k))'''
        # helper function
        def is_anagram(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            
            count_s1, count_s2 = {}, {}
            for i in range(len(s1)):
                count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
                count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)

            return count_s1 == count_s2

        # main algorithm
        group = []
        l = 0
        input_length = len(strs)
        seen = set()
        while l != input_length-1: # iterate through strs except the last one
            if strs[l] not in seen:
                temp = [strs[l]]
                seen.add(strs[l])
                for r in range(l+1, input_length): # probe through the rest
                    if is_anagram(strs[l], strs[r]):
                        temp.append(strs[r])
                        seen.add(strs[r])
                group.append(temp)
            l += 1

        # check for the last one that was skipped in strs
        if strs[-1] not in seen:
            group.append([strs[-1]])
        return group

        '''better solution (time: O(n*k), space: O(n*k))'''
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()