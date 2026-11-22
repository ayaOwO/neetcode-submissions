class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for value in tokens:
            res = value
            match value:
                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    res = a + b
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    res = a - b
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    res = a / b
                case "*":
                    res = stack.pop() * stack.pop()
            stack.append(int(res))
        return stack.pop()