class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # ideal solution takes this into subproblems such that
        # optimal of left and right over k
        nums.append(1)
        nums = [1] + nums
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # print(dp)

        def solve(i, j):
            # print((i, j))
            if j-i <= 1:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            
            max_val = -1
            for k in range(i+1, j):
                max_val = max(max_val, solve(i, k) + solve(k, j) + nums[i]*nums[k]*nums[j])

            dp[i][j] = max_val
            return max_val

        solve(0, n-1)

        return dp[0][n-1]
            
