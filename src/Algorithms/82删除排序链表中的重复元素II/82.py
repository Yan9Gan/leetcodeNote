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


if __name__ == '__main__':
    S = Solution()
    list_node = create_list_node([1, 1, 2, 3, 4, 5, 5, 6])
    res = S.deleteDuplicates(list_node)
    print_list_node(res)
