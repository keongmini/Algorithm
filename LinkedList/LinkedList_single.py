
# 연결리스트를 이루고 있는 노드
class LinkedNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

# 연결리스트 구현
class LinkedList:
    def __init__(self):
        # 연결리스트의 시작과 끝 선언(둘다 아무것도 없을 경우 연결리스트 비어있음)
        self.head = None
        self.tail = None
    
    def addHead(self, val):
        if not(self.head or self.tail) :
            node = LinkedNode(val, None)
            self.head = node
            self.tail = node
        else:
            self.head = LinkedNode(val, self.head)
    
    def addTail(self, val):
        if not(self.head and self.tail) :
            node = LinkedNode(val, None)
            self.head = node
            self.tail = node
        else:
            node = LinkedNode(val,None)
            self.tail.next = node
            self.tail = node
        
    def deleteHead(self):
        try:
            self.head = self.head.next
        except AttributeError:
            print("It's Empty")
    
    # 마지막 숫자를 삭제하는 메소드는 단순연결리스트로 구현 불가
    # def deleteTail(self):
    #     if not(self.tail):
    #         raise EmptyError("It's Empty")
    #     else:   
    #         self.tail = None

    # 주어진 임의의 값 다음값 삭제
    def delete(self, value):
        try:
            node = value.next
            value.next = node.next
        except AttributeError:
            print("It's Empty")
            
    def search(self,value):
        try:
            node = self.head
            cnt = 0
            while node.next:
                cnt += 1
                if node.value == value:
                    return cnt
                node = node.next
        except AttributeError:
            print("It's Empty")

    def printAll(self):
        node = self.head
        nodeList = []
        while True:
            nodeList.append(node.value)
            if not(node.next):
                break
            node = node.next
        
        return nodeList


node = LinkedList()
node.addHead("front3")
node.addTail("back1")
node.addHead("front2")
node.addTail("back2")
node.addHead("front1")
node.addTail("back3")

node.deleteHead() # node.head.valye = "front1" 삭제

print(node.head.value)
node.delete(node.head) # node.haed.value = "front2" 의 다음값인 front3 삭제

print(node.search("front2")) # 1번째 값

print(node.printAll())

node.deleteHead()
node.deleteHead()
node.deleteHead()
node.delete(node.head)  # node.head.value = "back3" 의 다음값 = None : It's empty 출력

print(node.printAll())  # ["back3"]
