class Solution:
    def isValid(self, s: str) -> bool:
        def match(open, close):
            pairs = {
                '{': 0,
                '}': 0,
                "[": 1,
                "]": 1,
                "(": 2,
                ")": 2
            }
            return pairs[open] == pairs[close]
        
        open = set(["(", "{", "["])
        stack = []

        for char in s:
            if char in open:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                if not match(stack.pop(), char):
                    return False
        if len(stack) != 0:
            return False
        return True

        