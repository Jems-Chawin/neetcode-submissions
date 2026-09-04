class Solution:

    def encode(self, strs: List[str]) -> str:
        list_return = []
        for s in strs:
            list_return.append(f"{len(s)}#{s}")
        return "".join(list_return)

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
