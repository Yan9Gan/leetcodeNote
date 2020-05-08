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


if __name__ == '__main__':
    S = Solution()
    list_node = create_list_node([1])
    x = 0
    res = S.partition(list_node, x)
    print_list_node(res)
