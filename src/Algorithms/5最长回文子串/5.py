# -*- coding:utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in s] for _ in s]
        for i in range(size):
            dp[i][i] = True

        max_len = 1
        start = 0
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    if j-i+1 > max_len:
                        max_len = j-i+1
                        start = i

        return s[start: start+max_len]


if __name__ == '__main__':
    S = Solution()
    s = 'aaaa'
    res = S.longestPalindrome(s)
    print(res)
