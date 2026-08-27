from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            elif bracket == ")" and (stack.pop() != "(" if stack else True):
                return False
            elif bracket == "]" and (stack.pop() != "[" if stack else True):
                return False
            elif bracket == "}" and (stack.pop() != "{" if stack else True):
                return False
                    
        return not stack