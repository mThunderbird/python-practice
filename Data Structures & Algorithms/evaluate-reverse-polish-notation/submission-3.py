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
            try:
                operand = int(token)
                operand_stack.append(operand)
            except ValueError:
                b, a = operand_stack.pop(), operand_stack.pop()
                result = operator_map[token](a, b)
                operand_stack.append(result)

        
        return operand_stack[-1]
    

