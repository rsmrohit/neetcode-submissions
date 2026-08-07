from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        result = [[]]

        for num, freq in count.items():
            new_subsets = []
            for subset in result:
                for i in range(1, freq + 1):
                    new_subsets.append(subset + [num] * i)
            result.extend(new_subsets)

        return result

        
        