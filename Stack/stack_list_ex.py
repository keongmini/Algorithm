# 파이썬으로 배우는 자료구조 p.76

def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0:
        return stack[-1]

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

stack = []
