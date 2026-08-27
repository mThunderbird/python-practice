from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        operator_map = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b)
        }

        operand_stack = deque()

        for token in tokens:
            if token in operator_map:
                b, a = operand_stack.pop(), operand_stack.pop()
                result = operator_map[token](a, b)
                operand_stack.append(result)
            else:
                operand_stack.append(int(token))

        
        return operand_stack[-1]
    

