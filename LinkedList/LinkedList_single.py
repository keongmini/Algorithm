
# 연결리스트를 이루고 있는 노드
class LinkedNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

# 연결리스트 구현
class LinkedList:
    def __init__(self):
        # 연결리스트의 시작과 끝 선언(둘다 아무것도 없을 경우 연결리스트 비어있음)
        self.first = None
        self.last = None
    
    def addfirst(self, val):
        if not(self.first or self.last) :
            node = LinkedNode(val, None)
            self.first = node
            self.last = node
        else:
            self.first = LinkedNode(val, self.first)
    
    def addlast(self, val):
        if not(self.first and self.last) :
            node = LinkedNode(val, None)
            self.first = node
            self.last = node
        else:
            node = LinkedNode(val,None)
            self.last.next = node
            self.last = node
        
    def deletefirst(self):
        try:
            self.first = self.first.next
        except AttributeError:
            print("It's Empty")
    
    # 마지막 숫자를 삭제하는 메소드는 단순연결리스트로 구현 불가
    # def deletelast(self):
    #     if not(self.last):
    #         raise EmptyError("It's Empty")
    #     else:   
    #         self.last = None

    # 주어진 임의의 값 다음값 삭제
    def delete(self, value):
        try:
            node = value.next
            value.next = node.next
        except AttributeError:
            print("It's Empty")
            
    def search(self,value):
        try:
            node = self.first
            cnt = 0
            while node.next:
                cnt += 1
                if node.value == value:
                    return cnt
                node = node.next
        except AttributeError:
            print("It's Empty")

    def printAll(self):
        node = self.first
        nodeList = []
        while True:
            nodeList.append(node.value)
            if not(node.next):
                break
            node = node.next
        
        return nodeList


node = LinkedList()
node.addfirst("front3")
node.addlast("back1")
node.addfirst("front2")
node.addlast("back2")
node.addfirst("front1")
node.addlast("back3")

node.deletefirst() # node.first.valye = "front1" 삭제

print(node.first.value)
node.delete(node.first) # node.haed.value = "front2" 의 다음값인 front3 삭제

print(node.search("front2")) # 1번째 값

print(node.printAll())

node.deletefirst()
node.deletefirst()
node.deletefirst()
node.delete(node.first)  # node.first.value = "back3" 의 다음값 = None : It's empty 출력

print(node.printAll())  # ["back3"]
