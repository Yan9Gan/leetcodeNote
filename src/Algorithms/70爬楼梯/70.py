# -*- coding:utf-8 -*-
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n

        stack = [0] * n
        stack[0] = 1
        stack[1] = 2
        for index in range(2, n):
            stack[index] = stack[index-1] + stack[index-2]

        return stack[-1]


if __name__ == '__main__':
    S = Solution()
    n = 3
    res = S.climbStairs(n)
    print(res)
