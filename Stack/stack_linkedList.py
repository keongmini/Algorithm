class Node:
    def __init__(self, node, next):
        self.node = node
        self.next = next

class Stack:
    def __init__(self):
        self.head = Node(None,None)
        self.tail = Node(None,None)

    def push(self, item):
        item_node = Node(item, None)

        if not(self.head.node):
            self.head.node = item_node
            self.tail.node = item_node
            self.head.node.next = self.tail
            return

        self.tail.next = item_node
        self.tail = item_node

    def pop(self):
        if not (self.head.node):
            return -1

        start = self.head
        while True:
            if start.next == self.tail:
                start.next = None
                self.tail == start
                return

            start = start.next

    def peek(self):
        if not(self.head):
            return -1
        return self.tail.node

    def size(self):
        self.cnt = 0

        start = self.head
        while True:
            if not(start):
                return
            self.cnt += 1
            start = start.next

        return self.cnt



stack = Stack()

stack.pop()
stack.peek()        # 빈리스트에 대한 작동 확인

stack.push(1)
stack.push(2)
stack.push(3)

stack.pop()
stack.peek()
stack.pop()
stack.peek()

print(stack.size())




