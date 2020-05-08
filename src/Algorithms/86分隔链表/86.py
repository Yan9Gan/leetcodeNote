# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new = ListNode(None)
        new.next = head
        pre = new
        stack = list()
        last = None
        while head:
            last = head
            if head.val >= x:
                if head.next:
                    pre.next = head.next
                else:
                    last = pre
                stack.append(head.val)
            else:
                pre = head

            head = head.next

        for item in stack:
            last.next = ListNode(item)
            last = last.next

        return new.next
