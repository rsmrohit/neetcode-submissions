class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        inds = {i:idx for idx, i in enumerate(nums)}

        for idx, i in enumerate(nums):
            try:
                ab = [idx, inds[target-i]]
                if ab[0] != ab[1]:
                    return ab
            except:
                continue
        return [0, 0]