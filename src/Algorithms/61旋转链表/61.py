# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        new = ListNode(None)
        new.next = head
        temp = head
        # 计算长度
        length = 0
        while temp.next and temp.next.val is not None:
            length += 1
            temp = temp.next

        last = temp
        count = k % (length+1)
        # 旋转 count 次
        for i in range(count):
            # 得到last_pre节点
            last_pre = new
            for i in range(length):
                last_pre = last_pre.next
            # 解链、链接过程
            temp = new
            last_pre.next = last.next
            last.next = temp.next
            temp.next = last
            # 重置last
            last = last_pre

        return new.next
