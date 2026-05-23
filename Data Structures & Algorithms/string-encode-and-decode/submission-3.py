class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            str_len = len(s)
            res += str(str_len) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        counter = 0

        while counter < len(s):
            j = counter
            while s[j] != "#":
                j += 1
            dist = int(s[counter: j])
            res.append(s[j + 1: j + 1 + dist])
            counter = j + 1 + dist
        
        return res


                

