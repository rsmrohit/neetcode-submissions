func maxCoins(nums []int) int {
    
    nums = append([]int{1}, nums...)
    nums = append(nums, 1)
    n := len(nums)

    dp := make([][]int, n)

    for i := range dp {
        dp[i] = make([]int, n)
    }

    for r, row := range dp{
        for c, _ := range row{
            dp[r][c] = 0
        }
    }

    var solve func(int, int) int
    solve = func(i int, j int) int{

        if j-i == 1 { return 0 }
        if dp[i][j] > 0 { return dp[i][j] }

        for k := i+1; k < j; k++ {
            val := solve(i, k) + solve(k, j) + nums[i]*nums[j]*nums[k]
            dp[i][j] = max(dp[i][j], val)
        }

        return dp[i][j]
    }

    return solve(0, n-1)

}
