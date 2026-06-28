import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocess
        clean = "".join(c for c in s if c.isalnum()).lower()
        return clean == clean[::-1]