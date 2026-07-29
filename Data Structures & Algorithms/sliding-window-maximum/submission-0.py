from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        rm = []

        for idx, i in enumerate(nums):

            # back-pruning: remove smaller-or-equal values from the back
            while stack and stack[-1][0] <= i:
                stack.pop()

            stack.append([i, idx])

            # front-eviction: remove stale indices from the front
            while stack and stack[0][1] <= idx - k:
                stack.popleft()

            # only record once the window is full
            if idx >= k - 1:
                rm.append(stack[0][0])

        return rm