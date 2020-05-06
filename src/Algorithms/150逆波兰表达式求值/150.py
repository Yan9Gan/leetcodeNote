# -*- coding:utf-8 -*-
from typing import List, Union


class Solution:
    def evalRPN(self, tokens: List[str]) -> Union[str, float]:
        stack = list()

        for item in tokens:
            if item not in ['+', '-', '*', '/']:
                stack.append(item)
            else:
                second, first = int(stack.pop()), int(stack.pop())
                print(second, first)
                if item == '+':
                    first += second
                elif item == '-':
                    first -= second
                elif item == '*':
                    first *= second
                else:
                    first /= second
                stack.append(first)

        return stack[0]
