class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        res = 0
        for t in tokens:
            if t in ['+', '-','*', '/']:
                if t == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                if t == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b - a)
                if t == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                if t == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b / a)

            else:
                stack.append(t)
        return int(stack[0])
