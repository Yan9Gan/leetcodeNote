# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        stack = list()
        repeat_stack = list()
        while head:
            if head.val in repeat_stack:
                pass
            elif head.val in stack:
                idx = stack.index(head.val)
                stack.pop(idx)
                repeat_stack.append(head.val)
            else:
                stack.append(head.val)

            head = head.next

        if stack:
            new = ListNode(None)
            temp = new
            for item in stack:
                temp.next = ListNode(item)
                temp = temp.next
            return new.next
        else:
            return None
