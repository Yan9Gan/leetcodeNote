# -*- coding:utf-8 -*-
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x < 10:
            return True

        x = str(x)
        left = 0
        right = len(x)-1
        while 1:
            if left >= right:
                break

            if x[left] != x[right]:
                return False

            left += 1
            right -= 1

        return True
