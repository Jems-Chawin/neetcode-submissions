class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect_dict = defaultdict(list)
        for s in strs:
            # 26 ตัวอักษรมี idx ของมัน
            alphabet_idx_lst = [0] * 26
            for c in s:
                # นับ occurence ไว้ที่ idx ของมัน
                alphabet_idx_lst[ord(c) - ord("a")] += 1
            # เก็บไว้ใน group เดียวกัน ซึ่งดูได้จาก list ของ occurence
            collect_dict[tuple(alphabet_idx_lst)].append(s)
        return list(collect_dict.values())