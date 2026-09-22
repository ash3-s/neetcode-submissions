class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if stack and len(stack) > 1 and t in ["+", "-", "*", "/"]:
                if t == "+":
                    stack.append(stack.pop() + stack.pop())
                elif t == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif t == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[0]