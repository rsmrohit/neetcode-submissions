from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache(maxsize=None)
        def traverse(i_s, i_p):
            if i_p == len(p):
                return i_s == len(s)

            first_match = i_s < len(s) and (p[i_p] == s[i_s] or p[i_p] == ".")

            if i_p + 1 < len(p) and p[i_p + 1] == "*":
                opt1 = traverse(i_s, i_p + 2)
                opt2 = first_match and traverse(i_s + 1, i_p)
                return opt1 or opt2
            else:
                return first_match and traverse(i_s + 1, i_p + 1)

        return traverse(0, 0)