class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += str(len(word)) + "#" + word
        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        length = ""
        ret = []
        while i < len(s):
            if s[i] != "#":
                length += s[i]
                i += 1
            elif s[i] == "#":
                start = i+1
                end = i+int(length)+1
                ret.append(s[start:end])
                i += int(length)+1
                length = ""
        return ret
        
