class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
       
        s1_seen = [0] * 26
        s2_seen = [0] * 26
        l, matches= 0, 0

        for i in range(len(s1)):
            s1_seen[ord(s1[i]) - ord('a')] += 1
            s2_seen[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if s1_seen[i] == s2_seen[i]:
                matches += 1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            curr_index = ord(s2[r]) - ord('a')
            s2_seen[curr_index] += 1
            if s2_seen[curr_index] == s1_seen[curr_index]:
                matches += 1
            elif s2_seen[curr_index] == s1_seen[curr_index] + 1:
                matches -= 1
            
            l_index = ord(s2[l]) - ord('a')
            s2_seen[l_index] -= 1
            if s2_seen[l_index] == s1_seen[l_index]:
                matches += 1
            elif s2_seen[l_index] == s1_seen[l_index] - 1:
                matches -= 1
            l += 1

        return matches == 26
