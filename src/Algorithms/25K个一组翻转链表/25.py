# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        new = ListNode(None)
        new.next = head
        index = 0
        pre = new
        while head:
            stack = list()
            # 取余等于0表示翻转的开头
            if index == 0 or index%k == 0:
                temp = head
                for i in range(k):
                    # 不够k个节点，不能翻转
                    if not temp:
                        index += 1
                        break
                    stack.append(temp)
                    temp = temp.next
                # 可翻转
                else:
                    last = temp
                    while stack:
                        item = stack.pop()
                        head = item
                        pre.next = head
                        pre = head
                        head.next = last
                    else:
                        head = head.next
                    index += k
            else:
                pre = head
                head = head.next
                index += 1

        return new.next
