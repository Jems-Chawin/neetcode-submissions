class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_lst = []
        for s in strs:
            # เทคนิค คือ len + delimiter + string
            ret_lst.append(f"{len(s)}#{s}")
        return "".join(ret_lst)

    def decode(self, s: str) -> List[str]:
        ret_lst = []
        i = 0
        while i < len(s):
            # เหมือนใช้ two pointer
            j = i
            while s[j] != "#":
                j += 1
            # เล่นกับ idx ให้ถูกตัว
            length_int = int(s[i:j])
            start_idx = j + 1
            end_idx = j + 1 + length_int
            ret_lst.append(s[start_idx:end_idx])
            # มันเป็น interval แบบ [a,b)
            i = end_idx
        return ret_lst
