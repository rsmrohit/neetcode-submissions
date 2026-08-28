/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func buildTree(preorder []int, inorder []int) *TreeNode {
    
	// parameters are slices so its fine

	inmap := map[int]int{}

    for ind, val := range inorder{
        inmap[val] = ind
    }

    var buildFunc func(int, int) *TreeNode
    pre := 0
    buildFunc = func(li, ri int) *TreeNode{

        if ri < li {
            return nil
        }

        node := &TreeNode { Val: preorder[pre]}
        k := inmap[preorder[pre]]
        pre++

        // left_size := k-li
        node.Left = buildFunc(li, k-1)
        node.Right = buildFunc(k+1, ri)
        return node
    }

    return buildFunc(0, len(inorder)-1)
}
