
// h[0] == amt, h[1] == # coins
type PH [][2]int

func (h PH) Len() int 				{return len(h)}
func (h PH) Less(i, j int) bool		{return h[i][1] < h[j][1]}
func (h PH) Swap(i, j int)			{h[i], h[j] = h[j], h[i]}

func (h *PH) Push (x any) {
	*h = append(*h, x.([2]int))
}

func (h *PH) Pop() any {
	old := *h
	n := len(old)
	*h = old[0:n-1]
	return old[n-1]
}

// Approach 1 heap fail because of out of memory error

func coinChange(coins []int, amount int) int {
    // So lets do a bfs with states representing (curr_amt, curr_#_coins)
	// Since we dont care about the type of coins being used we can run this algorithm to find the best solution, we can use a heap ordered on, curr_# coins, such that we find optimal as soon as possible 

	// This approach misses out memory because we keep too many states and repeat states in memory, we can have dictionary keyed on the amount to keep track of repeats, or we swap the solution to dp solution where we build up the table from previous amounts or top down where we start from top and go down ints

	dict := map[int]int{}

	h := &PH{}
	heap.Init(h)

	if amount == 0 {return 0}

	for i:=0; i < len(coins); i++ {
		heap.Push(h, [2]int{coins[i], 1})
		dict[coins[i]] = 1
	}

	for h.Len() > 0 {

		state := heap.Pop(h).([2]int)
		
		if state[0] == amount{
			return state[1]
		}

		for i:=0 ; i < len(coins); i++ {
			new_val := state[0] + coins[i]
			_, exists := dict[new_val]
			if new_val <= amount && !exists{
				heap.Push(h, [2]int{new_val, state[1]+1})
				dict[new_val] = state[1]+1
			}
		}
	}

	return -1
	

}


