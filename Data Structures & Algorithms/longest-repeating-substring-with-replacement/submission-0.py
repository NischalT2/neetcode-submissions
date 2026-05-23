class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        curr_len = 0
        res = 0
        freq_hash = defaultdict(int)

        for right in range(len(s)):
            freq_hash[s[right]] += 1
            curr_len += 1

            max_freq = max(freq_hash.values())

            if curr_len - max_freq > k:
                freq_hash[s[left]] -= 1
                curr_len -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res