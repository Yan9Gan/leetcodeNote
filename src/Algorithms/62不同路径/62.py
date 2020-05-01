# -*- coding:utf-8 -*-
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        temp_list = [[0 for j in range(m)] for i in range(n)]
        # 初始化
        temp_list[0][0] = 0
        for i in range(m):
            temp_list[0][i] = 1
        for i in range(n):
            temp_list[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                temp_list[i][j] = temp_list[i-1][j] + temp_list[i][j-1]

        return temp_list[n-1][m-1]


if __name__ == '__main__':
    S = Solution()
    m = 7
    n = 3
    res = S.uniquePaths(m, n)
    print(res)
