class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        starting_brackets = set(['{', '[', '('])
        matching_pairs = {'{': '}', '[':']', '(': ')'}
        for bracket in s:
            if bracket in starting_brackets:
                stack.append(bracket)
            else:
                if len(stack) > 0:
                    last_bracket = stack.pop()
                    if matching_pairs[last_bracket] != bracket:
                        return False
                else:
                    return False

        return len(stack) == 0

        