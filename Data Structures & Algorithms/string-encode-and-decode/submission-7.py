class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        to_return = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            int_length = int(s[i:j])
            temp = s[j+1:j+1+int_length]
            to_return.append(temp)
            i = j+1+int_length
        return to_return
