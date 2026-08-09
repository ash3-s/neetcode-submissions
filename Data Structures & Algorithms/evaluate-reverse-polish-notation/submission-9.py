class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if t in operators:
                if t == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                
                elif t == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b) - int(a))

                
                elif t == '*':
                    stack.append(int(stack.pop()) * int(stack.pop())) 
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack[-1]


