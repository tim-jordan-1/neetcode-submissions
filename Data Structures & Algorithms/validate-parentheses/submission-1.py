class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = set(["(","[","{"])
        map ={
            "(":0,
            ")":0,
            "[":1,
            "]":1,
            "{":2,
            "}":2
        }
        for val in s:
            if val in open:
                stack.append(val)
            elif len(stack) ==0:
                return False
            else:
                open_val = stack.pop()
                if map[open_val] != map[val]:
                    return False
        if len(stack) != 0:
            return False
        return True
                
