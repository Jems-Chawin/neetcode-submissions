class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        list_return = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            int_length = int(s[i:j])
            str_temp = s[j+1:j+1+int_length]
            list_return.append(str_temp)
            i = j+1+int_length
        return list_return
