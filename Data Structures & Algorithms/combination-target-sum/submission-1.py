class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if we think about it as a tree then it is pretty simple

        # at each node we can include the current number in the sum, or go to the next number

        cache = []

        def expand(summ, curr, i):
            nonlocal cache
            # print(summ, curr, i)

            if summ == target:
                cache.append(curr)
                return
            
            if summ + nums[i] <= target:
                expand(summ + nums[i], curr + [nums[i]], i)
            if i + 1 < len(nums):
                expand(summ, curr, i + 1)

        expand(0, [], 0)
        return cache

        