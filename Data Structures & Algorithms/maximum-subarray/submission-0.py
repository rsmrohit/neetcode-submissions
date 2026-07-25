class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # every subarray n-m can be represented as
        # the sum of 0-m - 0-n
        # therefore all we need to do is check a combination of mxn
        # where m and n is len of nums


        # nvm we use a sliding windows approach
        
        max_sum = nums[0]
        curr_win = 0
        window = [0, 0]

        while window[1] < len(nums):

            curr_win += nums[window[1]]
            max_sum = max(max_sum, curr_win)

            if curr_win < 0:
                curr_win = 0
            
            window[1] += 1
        
        return max_sum


