class Solution:

    def encode(self, strs: List[str]) -> str:
        list_res = []
        for str_s in strs:
            list_res.append(f"{len(str_s)}#{str_s}")
        return "".join(list_res)

    def decode(self, str_s: str) -> List[str]:
        list_return = []
        int_i = 0
        while int_i < len(str_s):
            int_j = int_i
            while str_s[int_j] != "#":
                int_j += 1
            int_length = int(str_s[int_i:int_j])
            str_temp = str_s[int_j+1:int_j+1+int_length]
            list_return.append(str_temp)
            int_i = int_j+1+int_length
        return list_return
