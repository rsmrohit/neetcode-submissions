from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Since a substring is a sort of window
        # we can use a variation of sliding windows
        # to solve this problem

        # the window here is the potential_substring
        # ps
        # since we care only abt len(ps), we can cache it
        # in an array at which ps started
        # in fact we wont even need a cache if we keep track of the maximum

        # this window will grow and shrink
        # it will shrink when it includes a duplicate letter
        # and it will grow when there is no duplicate letter

        # therefore all we need is a dict that keeps track of the dupes

        counter = defaultdict(int)
        ps_len = 0
        ps_max = 0
        ps_left = 0

        for l in s:
            # Grow phase
            ps_len += 1
            counter[l] += 1

            # Shrink phase only occurs when one dupe is found
            # therefor a single execution suffices
            while counter[l] > 1:
                counter[s[ps_left]] -= 1
                ps_left += 1
                ps_len -= 1
            
            ps_max = max(ps_len, ps_max)

        return ps_max



