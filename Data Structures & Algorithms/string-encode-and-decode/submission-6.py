import re

# str_output = re.sub(regex_search_term, regex_replacement, str_input)


class Solution:

    def encode(self, strs: List[str]) -> str:
        escaped = [re.sub(r"e", r"ee", word) for word in strs] # escape the escape
        escaped = [re.sub(r"d", r"ed", word) for word in escaped] # escape the delimiter
        encoded = ""
        for i in range(len(escaped)):
            encoded += escaped[i] + "d"

        return encoded

    def decode(self, s: str) -> List[str]:
        print("Input: [" + s + "]")
        decoded = s
        decoded = re.split(r"(?<!e)d|(?<!eee)(?<=ee)d", decoded) # if you see `eed` or just `d` split
        decoded = decoded[:-1]
        decoded = [re.sub(r"ed", "d", word) for word in decoded] # revert d escape
        decoded = [re.sub(r"ee", "e", word) for word in decoded] # revert e escape
        return decoded
                

