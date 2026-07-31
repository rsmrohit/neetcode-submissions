class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # we know its rotated, so the peak will either be on the right side
        # or on the left

        # but we dont need to do all that,
        # the essence of binary search is to simply split the search radius into two
        
        # this is if we have a target, we want to find min
        # so we check, target == middle -> return good
        # target > middle
        #   target < right -- left, right = middle, target
        #       -- left, right = left, middle
        # target < middle
        #   target > left -- left, right = left, middle
        #       -- left, right = middle, target

        # while middle != left
        #   middle > right -- left, right = middle, right
        #   middle < left -- left, right = left, middle

        left, right = 0, len(nums) - 1
        middle = (right + left) // 2

        while left < right:
            # print(left, middle, right)
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
            
            middle = (left + right) // 2
        
        return nums[left]