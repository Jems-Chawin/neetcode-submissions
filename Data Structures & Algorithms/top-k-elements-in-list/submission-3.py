class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using hashmap
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        # sort by values then reverse it
        ret = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        # return as a list up to k elements
        return list(ret.keys())[:k]