# -*- coding:utf-8 -*-
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list_node(l):
    list_node = ListNode(None)
    temp = list_node
    for item in l:
        temp.next = ListNode(item)
        temp = temp.next

    return list_node.next


def print_list_node(list_node):
    s_list = list()
    while list_node:
        s_list.append(str(list_node.val))
        list_node = list_node.next

    print(' -> '.join(s_list))


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        if length == 0:
            return None

        if length == 1:
            return lists[0]

        mid = length // 2

        return self.core(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:length]))

    def core(self, l1, l2):
        new = ListNode(None)
        temp = new
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            if val1 < val2:
                temp.next = ListNode(val1)
                l1 = l1.next
            elif val2 < val1:
                temp.next = ListNode(val2)
                l2 = l2.next
            else:
                temp.next = ListNode(val1)
                temp = temp.next
                temp.next = ListNode(val2)
                l1 = l1.next
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return new.next


if __name__ == '__main__':
    S = Solution()
    lists = [
        create_list_node([1, 4, 5]),
        create_list_node([1, 3, 4]),
        create_list_node([2, 6])
    ]
    res = S.mergeKLists(lists)
    print_list_node(res)
