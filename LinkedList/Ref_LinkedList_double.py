class DList:
    # 노드 생성자
    class Node :
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next
    
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self) : return self.size
    def is_empty(self) : return self.size == 0      # self.size 가 0일때 True를 반환하는 것으로 추정..

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)       
        p.prev = n
        t.next = n
        self.size +=1
    
    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t)       
        p.next = n
        t.prev = n
        self.size +=1

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size += 1
        return x.item
    
    def print_list(self):
        if self.is_empty():     # 비어있을 때 is_empty() -> True
            print("Empty list")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, "<=> ", end = '')
                else:
                    print(p.item)
                p = p.next


if __name__ == "__main__":
    s = DList()
    s.insert_after(s.head, "apple")
    s.insert_before(s.tail, "orange")
    s.insert_before(s.tail, "cherry")
    s.insert_after(s.head.next, "pear")
    s.print_list()
    print("After delete last node :\t", end = '')
    s.delete(s.tail.prev)
    s.print_list()
    print("After insert grape the very end\t", end = '')
    s.insert_before(s.tail,"grape")
    s.print_list()
    print("After delete first node\t", end = '')
    s.delete(s.head.next)
    s.print_list()
    print("After delete first node\t", end = '')
    s.delete(s.head.next)
    s.print_list()
    print("After delete first node\t", end = '')
    s.delete(s.head.next)
    s.print_list()
    print("After delete first node\t", end = '')
    s.delete(s.head.next)
    s.print_list()
    