class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_mem = [[-1] * len(s) for _ in range(len(s))]
        max_len = 1
        max_len_word = (0, 0)

        def traverse(i, j):
            nonlocal max_len
            nonlocal max_len_word

            if i < 0 or i >= len(s):
                return
            if j < 0 or j >= len(s):
                return
            if i > j:
                return
            if s_mem[i][j] > -1:
                return

            # Base cases
            if i == j:
                s_mem[i][j] = 1
                return
            if abs(i - j) == 1 and s[i] == s[j]:
                s_mem[i][j] = 2
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_len_word = (i, j)
                return

            traverse(i + 1, j - 1)

            if s[i] == s[j] and s_mem[i + 1][j - 1] > 0:
                s_mem[i][j] = s_mem[i + 1][j - 1] + 2
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_len_word = (i, j)
            else:
                s_mem[i][j] = 0

        for i in range(len(s)):
            for j in range(len(s)):
                traverse(i, j)

        return s[max_len_word[0]:max_len_word[1] + 1]