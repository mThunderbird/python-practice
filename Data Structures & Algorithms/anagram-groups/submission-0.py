class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagram code -> [ words ]
        hmap = {}

        for word in strs:
            table = [0 for i in range(0, 26)]
            for letter in word:
                table[ord(letter) - ord('a')] += 1
            code = str(table)
            if code not in hmap:
                hmap[code] = list()
            hmap[code].append(word)
        
        return list(hmap.values())