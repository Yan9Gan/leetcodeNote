# -*- coding:utf-8 -*-
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        stack = list()
        dp = [0 for _ in s]

        index = 0
        while index < len(s):
            item = s[index]

            if stack and item==')' and stack[-1][0]=='(':
                dp[stack[-1][1]] += 1
                if stack[-1][1]-1 >= 0 and dp[stack[-1][1]-1]:
                    dp[stack[-1][1]] += dp[stack[-1][1]-1]
                dp[index] += 1+dp[index-1]
                if index-stack[-1][1] > 1:
                    dp[index] += dp[stack[-1][1]]
                stack.pop(-1)
            else:
                stack.append([item, index])

            index += 1

        return max(dp)
