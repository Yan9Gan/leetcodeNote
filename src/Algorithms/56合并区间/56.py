# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return list()

        intervals = sorted(intervals, key=lambda x:x[0])
        new = list()
        for index, item in enumerate(intervals):
            if not new:
                new.append(item)
                continue

            for new_index, new_item in enumerate(new):
                if new_item[0] <= item[0] <= new_item[1]:
                    if new_item[0] <= item[1] <= new_item[1]:
                        pass
                    else:
                        new[-1][1] = item[1]
                    break
                elif item[0] <= new_item[0] <= item[1]:
                    if item[0] <= new_item[1] <= item[1]:
                        new[new_index] = item
                    else:
                        new[new_index] = [item[0], new_item[1]]
                    break
            else:
                new.append(item)

        return new
