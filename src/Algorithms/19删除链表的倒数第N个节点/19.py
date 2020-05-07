# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new = ListNode(None)
        new.next = head
        pre = new
        while head:
            temp = head
            for i in range(n):
                temp = temp.next
            if not temp:
                pre.next = head.next
                break

            pre = head
            head = head.next

        return new.next


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


if __name__ == '__main__':
    S = Solution()
    list_node = create_list_node([1, 2, 3, 4, 5])
    n = 2
    res = S.removeNthFromEnd(list_node, n)
    print_list_node(res)
