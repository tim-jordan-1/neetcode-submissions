class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def parenthesis(subset, l, r):
            if l == 0 and r == 0:
                res.append(subset)
                return
            
            if l == r:
                parenthesis(subset + "(", l-1, r)
            elif r > l and l != 0:
                parenthesis(subset + "(", l-1, r)
                parenthesis(subset + ")", l, r-1)
            else:
                parenthesis(subset + ")", l, r-1)
        
        parenthesis("", n, n)
        return res