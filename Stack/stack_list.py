class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        if len(self.stack_list) == 0:
            return -1
        self.stack_list.pop()

    def peek(self):
        if len(self.stack_list) == 0:
            return -1
        return self.stack_list[-1]

    def check(self):
        return self.stack_list

stack = Stack()
stack.pop()         # 빈 리스트 확인하기
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.peek()
stack.pop()
stack.peek()

print(stack.check())