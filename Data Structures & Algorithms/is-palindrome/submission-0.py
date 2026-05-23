class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_lower = s.lower()
        left, right = 0, len(str_lower) - 1

        while left < right:
            if not str_lower[left].isalnum():
                left += 1
                continue
            if not str_lower[right].isalnum():
                right -= 1
                continue
            if str_lower[left] != str_lower[right]:
                return False
            left += 1
            right -= 1
        return True