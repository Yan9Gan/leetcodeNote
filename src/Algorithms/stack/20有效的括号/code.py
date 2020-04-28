# -*- coding:utf-8 -*-
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False

        brackets_dict = {
            ')': '(', ']': '[', '}': '{'
        }
        temp_stack = list()
        for item in s:
            if item in brackets_dict.values():
                temp_stack.append(item)
            else:
                if temp_stack and temp_stack[-1] == brackets_dict[item]:
                    temp_stack.pop(-1)
                else:
                    temp_stack.append(item)

        if not temp_stack:
            return True
        return False
