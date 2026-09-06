from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # classic two pointer question with growing window
        count_t = defaultdict(int)

        # initialize
        for l in t:
            count_t[l] += 1 
        
        # always keeps only whats required
        count_w = defaultdict(int)
        len_w = 0
        len_cw = 0

        l, r = 0, 0
        minLenSub = [float('inf'), 0, -1]

        while r < len(s):

            # print(minLenSub, l, r)

            sr = s[r]

            len_w += 1
            if count_t[sr] > 0:
                count_w[sr] += 1

                if count_w[sr] <= count_t[sr]:
                    len_cw += 1
            
            
            while len_cw == len(t):

                # update min since we matched
                if len_w < minLenSub[0]:
                    minLenSub[0]  = len_w
                    minLenSub[1]  = l
                    minLenSub[2]  = r

                sl = s[l]
                
                len_w -= 1
                if count_w[sl] > 0:
                    count_w[sl] -= 1

                    if count_w[sl] < count_t[sl]:
                        len_cw -= 1
                
                l += 1

            r += 1

        return s[minLenSub[1]:minLenSub[2]+1]

