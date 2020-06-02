# -*- coding:utf-8 -*-
class Solution:
    def sumNums(self, n: int) -> int:
        def core(num):
            if num == 1:
                return 1
            else:
                return core(num-1) + num

        return core(n)


if __name__ == '__main__':
    S = Solution()
    n = 3
    sum = S.sumNums(n)
    print(sum)
