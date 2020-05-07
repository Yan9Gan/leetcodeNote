# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
