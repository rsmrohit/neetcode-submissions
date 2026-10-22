class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically increasing stack, keep track of the next warmest day

        q = []
        ind = len(temperatures) - 1
        res = [0] * len(temperatures)

        while ind >= 0:
            while q and q[-1][0] <= temperatures[ind]:
                q.pop()

            if not q:
                res[ind] = 0
            elif q[-1][0] > temperatures[ind]:
                pos = q[-1][1] - ind
                res[ind] = pos

            q.append([temperatures[ind], ind])

            ind -= 1

        return res