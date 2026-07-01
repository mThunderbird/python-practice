class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        table = dict()
        for character in s:
            table[character] = table.get(character, 0) + 1
        for character in t:
            table[character] = table.get(character, 0) - 1
        
        return not any(v != 0 for v in table.values())
        