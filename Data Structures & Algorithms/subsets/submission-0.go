func subsets(nums []int) [][]int {

	var results [][]int
	n := len(nums)

	var solver func(pos int, subset []int)

	solver = func(pos int, subset []int) {
		if pos == n {
			subsetCopy := make([]int, len(subset))
			copy(subsetCopy, subset)
			results = append(results, subsetCopy)
			return
		}

		solver(pos + 1, append(subset, nums[pos]))
		solver(pos + 1, subset)
	}

	solver(0, []int{})
	return results
}
