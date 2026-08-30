class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''my attempt (time: O(k*n*logn))'''
        # using hashmap
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        # sort by values then reverse it
        ret = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        # return as a list up to k elements
        return list(ret.keys())[:k]

        '''better solution (time: O(n))'''
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
