class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            s_len = str(len(s))
            new_str += (s_len + "#" + s)
        
        return new_str

    def decode(self, s: str) -> List[str]:
        counter = 0
        res = []
        while counter < len(s):
            i = counter
            while s[i] != "#":
                i += 1
            s_len = int(s[counter: i])
            res.append(s[i + 1: i + 1 + s_len])
            counter = i + s_len + 1
        
        return res
