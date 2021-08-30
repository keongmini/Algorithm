class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode()
        add = 0 
        while l1 and l2:
            l1_val = l1.val
            l1 = l1.next

            l2_val = l2.val
            l2 = l2.next

            plus = (l1_val+l2_val)%10

            nextNode = node
            node = ListNode(plus+add, nextNode)

            add = (l1_val+l2_val)//10

        return node

if __name__ == "__main__":
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_1.next = l2_2
    l2_2.next = l2_3

    s = Solution()
    s.addTwoNumbers(l1_1, l2_1)