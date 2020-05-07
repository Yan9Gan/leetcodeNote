# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        index = 0
        new_list_node = ListNode(None)
        new_list_node.next = head
        pre = None
        pre_pre = new_list_node
        while head:
            # 偶数个交换（下标为奇数）
            if index % 2 != 0:
                # 交换
                pre_pre.next = head
                pre.next = head.next
                head.next = pre
                # 进入下一个
                pre_pre = head
                head = pre.next
            else:
                if index == 0:
                    pre = head
                    head = head.next
                else:
                    pre_pre = pre
                    pre = head
                    head = head.next

            index += 1

        return new_list_node.next
