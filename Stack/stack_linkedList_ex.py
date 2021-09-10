'''
파이썬으로 배우는 자료구조 p.77
[1,2,3,4] 에서 1 -> 2 -> 3 -> 4 로 보지 않고
4 -> 3-> 2 -> 1로 봄 : 노드의 next값을 자동으로 부여 가능
전역변수 global 용
'''

class Node:
    def __init__(self, item, link):
        self.item = item
        self.link = link

def push(item):
    global top
    global size
    top = Node(item,top)
    size += 1

def peek():
    if size != 0:
        return top.item

def pop():
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.next
        size -= 1
        return top_item

def print_stack():
    print('top -> \t', end="")
    p = top
    while p:
        if p.next != None:
            print(p.item, '-> ', end="")
        else:
            print(p.item, end="")
        p=p.next
    print()

top = None
size = 0
print_stack()