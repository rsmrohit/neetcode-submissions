class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # tree where we generate
        cache = []
        def gen_paren(i, stack, open_count):
            nonlocal cache

            if i == 0:
                cache.append(stack)
                return
            
            if open_count < i:
                gen_paren(i, stack + "(", open_count+1)

            if open_count > 0:
                gen_paren(i-1, stack + ")", open_count-1)
                
        gen_paren(n, "", 0)

        return cache