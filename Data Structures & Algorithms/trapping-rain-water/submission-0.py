class Solution:
    def trap(self, height: List[int]) -> int:
        # just build two increasing arrays, from left and right
        # then at each value find the min at that pos

        # since the value at each index would be min of greatest int from left and greatest int from right


        left = []
        right = []

        max_int = height[0]
        for i in height:
            max_int = max(i, max_int)
            left.append(max_int)
            
        
        max_int = height[-1]
        for i in height[::-1]:
            max_int = max(i, max_int)
            right.append(max_int)
        
        right = right[::-1]

        # print(left)
        # print(right)

        water = 0
        for idx in range(len(height)):
            water += min(left[idx], right[idx]) - height[idx]
        
        return water
        