class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(b/a))
                print(stack[-1])
            else:
                stack.append(int(t))
        
        return stack[-1]