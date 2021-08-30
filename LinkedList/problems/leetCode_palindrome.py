# https://leetcode.com/problems/palindrome-linked-list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        palin_list = []

        node = head

        if not(node):
            return True
        while node:
            palin_list.append(node.val)
            node = node.next

        while len(palin_list) > 0:
            if palin_list.pop(0) != palin_list.pop():
                return False
        
        return True

if __name__ == "__main__" :
    palin = Solution()
    head = ListNode(1,ListNode(2, None))

