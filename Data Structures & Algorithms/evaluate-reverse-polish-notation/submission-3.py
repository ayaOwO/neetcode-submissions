class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        for value in tokens:
            res = value
            match value:
                case "+":
                    res = stack.pop() + stack.pop()
                case "-":
                    b, a = stack.pop(), stack.pop()
                    res = a - b
                case "/":
                    b, a = stack.pop(), stack.pop()
                    res = a / b
                case "*":
                    res = stack.pop() * stack.pop()
            stack.append(int(res))
        return stack.pop()