class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","*","/"}
        for i in tokens:
            if i in operations:
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    stack.append(second + first)

                elif i == "-":
                    stack.append(second - first)

                elif i == "*":
                    stack.append(second * first)


                else:
                    stack.append(int(second / first)) 

            else:
                stack.append(int(i)) 
        return stack[-1]
