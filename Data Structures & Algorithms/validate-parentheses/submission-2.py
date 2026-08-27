from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }
                    
        for bracket in s:
            if bracket in closeToOpen:
                if not stack:
                    return False
                if stack.pop() != closeToOpen[bracket]:
                    return False
            else:
                stack.append(bracket)

        return not stack