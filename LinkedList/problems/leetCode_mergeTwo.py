# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        nodeValueList = ListNode(-1)
        node_list = nodeValueList
        
        while l1 and l2:

            if l1.val <= l2.val:
                node_list.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                node_list.next = l2
                l2 = l2.next
            
            node_list = node_list.next

        if l1:
            node_list.next = l1
        elif l2 :
            node_list.next = l2
        
        return nodeValueList.next


if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(3)
    l1_3 = ListNode(4)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(2)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3
                
    s = Solution()
    result = s.mergeTwoLists(l1_1, l2_1)