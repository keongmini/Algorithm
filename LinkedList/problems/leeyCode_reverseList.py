# https://leetcode.com/problems/reverse-linked-list/

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        tmp = None

        while node:
            nodeNext, node.next = node.next, tmp
            tmp, node = node, nodeNext

        return tmp

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    s = Solution()
    s.reverseList(n1)
            

            

            