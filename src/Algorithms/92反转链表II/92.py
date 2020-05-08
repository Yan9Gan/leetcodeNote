# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n or not head:
            return head

        new = ListNode(None)
        new.next = head
        index = 0
        pre = new
        while head:
            if index == m-1:
                stack = list()
                temp = head
                for i in range(n-m+1):
                    stack.append(temp)
                    temp = temp.next
                else:
                    # 翻转区间的下一个节点
                    last = temp
                    while stack:
                        curr = stack.pop()
                        head = curr
                        pre.next = head
                        pre = head
                        head.next = last
                    else:
                        head = head.next
                        index += n-m+1
            else:
                pre = head
                head = head.next
                index += 1

        return new.next
