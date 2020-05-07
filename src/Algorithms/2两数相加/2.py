# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list_node = ListNode(None)
        temp = new_list_node
        add = 0
        while l1 and l2:
            val1 = l1.val
            val2 = l2.val
            temp.next = ListNode((val1+val2+add)%10)
            add = (val1+val2+add) // 10
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            temp.next = ListNode((val+add) % 10)
            add = (val+add) // 10
            temp = temp.next
            l1 = l1.next
        while l2:
            val = l2.val
            temp.next = ListNode((val+add) % 10)
            add = (val+add) // 10
            temp = temp.next
            l2 = l2.next

        if add:
            temp.next = ListNode(add)

        return new_list_node.next
