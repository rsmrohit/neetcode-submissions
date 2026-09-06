class Solution:
    def checkValidString(self, s: str) -> bool:
        # what about pushing wildcards down

        # two stack solution
        o_stack = []
        w_stack = []

        for idx, p in enumerate(s):
            if p == "(":
                o_stack.append(idx)
            
            if p == "*":
                w_stack.append(idx)
            
            if p == ")":
                if len(o_stack) > 0:
                    o_stack.pop()
                elif len(w_stack) > 0:
                    w_stack.pop()
                else:
                    return False
        
        while o_stack:

            if w_stack and w_stack[-1] > o_stack[-1]:
                w_stack.pop()
                o_stack.pop()
            else:
                return False
        
        return len(o_stack) == 0
