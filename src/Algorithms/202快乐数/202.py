# -*- coding:utf-8 -*-
class Solution:
    def isHappy(self, n: int) -> bool:
        temp_list = list()

        def count(n):
            n_list = [int(i) for i in str(n)]
            sum = 0
            for item in n_list:
                sum += item ** 2

            return sum

        while n != 1 and n not in temp_list:
            temp_list.append(n)
            n = count(n)

        if n == 1:
            return True
        else:
            return False
