# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res_list = list()
        DIGITS_LIST = [i for i in digits]
        digits_list = [i for i in digits]
        if not digits_list:
            return res_list

        curr_digit = digits_list.pop(0)
        res = ''
        self.core_func(curr_digit, digits_list, res, res_list, DIGITS_LIST)

        return res_list

    def core_func(self, curr_digit, digits_list, res, res_list, DIGITS_LIST, count=0):
        digit_alpha_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        curr_alpha_list = digit_alpha_dict[curr_digit]
        while curr_alpha_list:
            alpha = curr_alpha_list.pop(0)
            if digits_list:
                curr_digit = digits_list.pop(0)
                self.core_func(curr_digit, digits_list, res + alpha, res_list, DIGITS_LIST, count+1)
            else:
                res_list.append(res + alpha)
        digits_list.insert(0, DIGITS_LIST[count])
