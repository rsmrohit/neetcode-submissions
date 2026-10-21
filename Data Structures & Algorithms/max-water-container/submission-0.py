class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left != right:

            max_area = max(max_area, (right - left) * min(heights[right], heights[left]))
            # print(left, right, heights[left], heights[right])

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            
        return max_area