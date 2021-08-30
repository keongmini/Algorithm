class CList:
    class Node:
        def __init__(self, item, next):
            self.item = item
            self.next = next
    
    def __init__(self):
        self.last = None
        self.size = 0
    
    def listSize(self): return self.size
    def is_empty(self): return self.size == 0

    def insert(self, item):
        n = self.Node(item, None)
        if self.is_empty():
            n.next = n          # 원형으로 이루어져있기 때문에 노드가 하나만 있을 경우 해당 노드의 다음 노드도 자신을 참조
            self.last = n
        else:
            n.next = self.last.next         # 삽입될 경우 self.last가 가리키는 노드쪽으로 삽입, self.last가 가리키고 있는 노드가 가장 최근 삽입된 노드
            self.last.next = n
        self.size += 1
    
    def first(self):
        if self.is_empty():
            print("Empty List")
        f = self.last.next
        return f.item
    
    def delete(self):                  # 가장 최근에 삽입된 노드 삭제
        if self.is_empty():
            print("Empty List")
        x = self.last.next
        if self.size == 1:
            self.last = None        # 하나있는 노드가 삭제됐음으로 전체 연결리스트가 비게 됨
        else:
            self.last.next = x.next
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("Empty List")
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, " -> ", end="")
                p = p.next
            print(p.item)

if __name__ == "__main__":
    s = CList()
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.print_list()
    print("lenghth : ", s.listSize())
    print("first node item = ", s.first())
    s.delete()
    print("After delete first node : ", end="")
    s.print_list()
    print("lenghth : ", s.listSize())
    print("first node item = ", s.first())
    s.delete()
    print("After delete first node : ", end="")
    s.print_list()
    s.delete()
    print("After delete first node : ", end="")
    s.print_list()
    s.delete()
    print("After delete first node : ", end="")
    s.print_list()
