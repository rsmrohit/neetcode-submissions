class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # use DP to keep track of prom this pos s_i, at ind_t j how many can I match

        # problem can be simplified into ways we can match s[i:] to t[j:]

        dp = [[-1 for _ in t] for _ in s]

        def compute_dp(i, j):

            if dp[i][j] > -1:
                return dp[i][j]
            
            summa = 0
            if s[i] == t[j]:
                if j == len(t) - 1:
                    summa = 1
                elif i < len(s) - 1:
                    summa = compute_dp(i+1, j+1)
        
            if i < len(s) - 1 and len(s) - i > len(t) - j:
                summa += compute_dp(i+1, j)
            
            dp[i][j] = summa
            return dp[i][j]

        compute_dp(0, 0)
        return dp[0][0]



                

            
            