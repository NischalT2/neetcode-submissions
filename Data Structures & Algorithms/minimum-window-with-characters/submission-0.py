class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        t_counter, window = {}, {}
        for c in t:
            t_counter[c] =  1 + t_counter.get(c, 0)

        have, need = 0, len(t_counter)
        res, resLen = [-1, -1], float("infinity")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in t_counter and t_counter[c] == window[c]:
                have += 1

                while have == need:
                    if (right - left + 1) < resLen:
                        res = [left, right]
                        resLen = right - left + 1

                    window[s[left]] -= 1
                    if s[left] in t_counter and window[s[left]] < t_counter[s[left]]:
                        have -= 1

                    left += 1
        
        left, right = res

        return s[left: right + 1] if resLen != float("infinity") else ""

                

