# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        index = 0
        new = list()
        while 1:
            if index == len(intervals):
                break

            add_flag = False
            if newInterval:
                if intervals[index][0] <= newInterval[0] <= intervals[index][1]:
                    if newInterval[1] > intervals[index][1]:
                        new.append([intervals[index][0], newInterval[1]])
                    else:
                        new.append(intervals[index])
                    add_flag = True
                    newInterval = []
                elif newInterval[0] < intervals[index][0]:
                    if newInterval[1] > intervals[index][1]:
                        new.append(newInterval)
                    elif newInterval[1] < intervals[index][0]:
                        new.append(newInterval)
                        new.append(intervals[index])
                    else:
                        new.append([newInterval[0], intervals[index][1]])
                    add_flag = True
                    newInterval = []

            if not add_flag:
                if new and new[-1][1] >= intervals[index][0]:
                    if new[-1][1] < intervals[index][1]:
                        new[-1][1] = intervals[index][1]
                else:
                    new.append(intervals[index])
            index += 1

        if newInterval:
            new.append(newInterval)

        return new
