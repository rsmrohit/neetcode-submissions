// import "container/heap"
// Len
// Less, idx_i, idx_j, -> bool
// Swap, idx_i, idx_j
// Push of pointer h *hp gets x any
// Pop of pointer h *hp returns any

type Cell struct {
	val int
	x int
	y int
}

type hp []Cell

func (h hp) Len() int { return len(h) }
func (h hp) Less(i int, j int) bool{ return h[i].val < h[j].val }
func (h hp) Swap(i int, j int) { h[i], h[j] = h[j], h[i] }

func (hpp *hp) Push(x any) {
	*hpp = append(*hpp, x.(Cell))
}

func (hpp *hp) Pop() any {
	n := len(*hpp)
	val := (*hpp)[n-1]
	*hpp = (*hpp)[:n-1]
	return val
}

func swimInWater(grid [][]int) int {
    // so this is going to be a simple bfs with heuristic problem
	// simple bfs with heap where heap is elevation

	n := len(grid)
	mh := &hp{Cell{val: grid[0][0], x: 0, y: 0}}
	heap.Init(mh)
	swim_dirs := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	// init a cache to keep track of cells we've reached
	// since bfs is optimal algorithimically we just need to make sure we dont re explore to avoid exponentiating
	// we'll use grid as cache since we dont care about re-exploration

	grid[0][0] = -1
	elevation := 0

	if n == 1 {
		return 0
	}

	for mh.Len() > 0 {
		target := heap.Pop(mh).(Cell)
		elevation = max(elevation, target.val)
		for _, row := range swim_dirs {
			new_x, new_y := row[0] + target.x, row[1] + target.y
			// check if new cell is in bounds and hasnt been explored
			if new_x > -1 && new_x < n && new_y > -1 && new_y < n && grid[new_x][new_y] != -1{
				
				heap.Push(mh, Cell{val: grid[new_x][new_y], x: new_x, y: new_y})
				
				if new_x == n-1 && new_y == n-1{
					return max(elevation, grid[new_x][new_y])
				}
				grid[new_x][new_y] = -1
			}

			
		}

	}

	return -1

}
