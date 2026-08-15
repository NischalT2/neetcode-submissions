class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            new_s = str(len(s)) + "#" + s
            encoded_string += new_s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            new_l = l
            while s[new_l] != "#":
                new_l += 1
            
            s_len = int(s[l:new_l])
            res.append(s[new_l+1: new_l + s_len + 1])
            l = new_l + s_len + 1
    
        return res
