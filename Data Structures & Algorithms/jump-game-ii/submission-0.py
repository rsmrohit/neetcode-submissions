class Solution:
    def jump(self, nums: List[int]) -> int:
        # bfs with memoization
        # store an array with the min jumps to get to position and run bfs from the start
        memo = [float('inf')] * len(nums)

        # actually if we're doing bfs we dont even need memoization because the first hit to the end is the min

        turns = 0
        discovered = set()
        stack = [(0, 0)]

        while stack:
            pos, turn = stack.pop(0)

            if pos == len(nums) - 1:
                return turn

            for i in range(nums[pos]):
                if pos + i + 1 not in discovered:
                    discovered.add(pos + i + 1)
                    stack.append((pos + i + 1, turn+1))
        
        return stack[0][1]
