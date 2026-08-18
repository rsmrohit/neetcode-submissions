func findOrder(numCourses int, prerequisites [][]int) []int {
    
    // classic dfs with three color system,
    // we'll build adjacency list with relationship course -> prereq
    // a: [b, ]
    // 0 -> 1
    // after we finish exploring one we push to list and publish that

    adj_list := make(map[int][]int)
    cache := make([]int, numCourses)
    order := []int{}

    for _, row := range prerequisites {
        adj_list[row[0]] = append(adj_list[row[0]], row[1])
    }

    var dfs func(node int) int

    dfs = func(node int) int {

        if cache[node] == 1{
            return -1
        }

        if cache[node] == 2{
            return 0
        }

        cache[node] += 1

        // dfs each path
        for len(adj_list[node]) > 0{

            next := adj_list[node][len(adj_list[node]) - 1]
            adj_list[node] = adj_list[node][:len(adj_list[node])-1]

            if dfs(next) == -1{
                return -1
            }

        }

        cache[node] += 1

        order = append(order, node)
        return 0
    }

    for i := 0; i < numCourses; i++ {
        if cache[i] == 0 {
            if dfs(i) == -1 {
                return []int{}
            }
        }
    }

    return order

}
