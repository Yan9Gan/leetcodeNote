# -*- coding:utf-8 -*-
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
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        cur, nxt = head, head.next
        new = ListNode(None)
        new.next = head
        while nxt:
            if nxt.val > cur.val:
                cur, nxt = nxt, nxt.next
            else:
                cur.next = nxt.next
                pre1, pre2 = new, new.next
                while nxt.val > pre2.val:
                    pre1, pre2 = pre2, pre2.next
                pre1.next = nxt
                nxt.next = pre2
                nxt = cur.next

        return new.next
