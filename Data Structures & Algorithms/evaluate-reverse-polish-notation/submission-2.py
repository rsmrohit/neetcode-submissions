class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tok = tokens.pop()
        
        if tok not in ("+", "-", "*", "/"):
            return int(tok)
        
        # print
        right = self.evalRPN(tokens)
        left = self.evalRPN(tokens)

        # print(right, left)
        if tok == "+": 
            return right + left
        if tok == "*":
            return right * left
        if tok == "-":
            return left - right
        if tok == "/":
            return int(left / right)