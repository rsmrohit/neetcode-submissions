from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_count = Counter(s1)
        win_count = Counter(s2[:n1])

        if win_count == s1_count:
            return True

        for i in range(n1, n2):
            win_count[s2[i]] += 1
            left_char = s2[i - n1]
            win_count[left_char] -= 1
            if win_count[left_char] == 0:
                del win_count[left_char]

            if win_count == s1_count:
                return True

        return False