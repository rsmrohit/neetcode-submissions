class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # this is a dp problem, max sum without being able to add next to each other

        # we can rep problem of len n as 
        # max(n-1, n + n-2)

        nums_cache = []
        
        for idx, i in enumerate(nums):
            # baseline
            if idx == 0:
                nums_cache.append(i)
                continue
            if idx == 1:
                nums_cache.append(max(nums[0], nums[1]))
                continue
            
            nums_cache.append(max(nums_cache[idx - 2] + i, nums_cache[idx - 1]))
            print(nums_cache)

        if len(nums_cache) > 1:
            return max(nums_cache[-1], nums_cache[-2])
        return nums_cache[-1]
