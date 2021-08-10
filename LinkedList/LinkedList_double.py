class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
    
    def add_before(self, node, value):
        insert_node = Node(value, None, None)
        if not(self.first) and not(self.last):
            self.first = insert_node
            self.last = insert_node
        else:
            _node = self.first
            while _node:
                if _node.value == node.value:
                    if _node == self.first:
                        self.first.prev = insert_node
                        insert_node.next = self.first
                        self.first = insert_node
                    else:
                        insert_node.prev = _node.prev
                        insert_node.next = _node
                        _node.prev.next = insert_node
                        _node.prev = insert_node
                    break
                _node = _node.next
        
    def add_after(self, node, value):
        insert_node = Node(value, None, None)
        if not(self.first) and not(self.last):
            self.first = node
            self.last = node
        else:
            _node = self.first
            while _node:
                if _node.value == node.value:
                    if _node == self.last:
                        insert_node.prev = self.last
                        self.last.next = insert_node
                        self.last = insert_node
                    else:
                        insert_node.prev = _node
                        insert_node.next = _node.next
                        _node.next.prev = insert_node
                        _node.next = insert_node
                    break
                _node = _node.next

    def delete(self, node):
        if not(self.first) and not(self.last):
            return "Empty"
        _node = self.first
        while _node:
            if _node.value == node:
                if _node == self.first:
                    _node.next.prev = None
                    self.first = _node.next
                elif _node == self.last:
                    _node.prev.next = None
                    self.last = _node.prev
                else:
                    _node.prev.next = _node.next
                    _node.next.prev = _node.prev
                break
            _node = _node.next

    def print_list(self):
        if not(self.first) and not(self.last):
            return "Empty"
        _node = self.first
        _nodeList = []
        while _node:
            _nodeList.append(_node.value)
            _node = _node.next
        return _nodeList


# ------------------------------------------ test

double = DoublyLinkedList()

print(double.print_list())
print(double.delete(3))

double.add_before(double.first, 2)
double.add_after(double.last, 8)
double.add_before(double.first, 1)
double.add_after(double.last, 9)
print(double.print_list())

double.delete(1)
double.delete(9)
print(double.print_list())