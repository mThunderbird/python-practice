import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocess
        s = s.lower()
        non_alphanum = re.compile(r"[^a-zA-Z0-9]")
        s = re.sub(non_alphanum, "", s)

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True