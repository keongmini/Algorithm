class Queue:
    def __init__(self):
        self.queue = []

    def add(self, item):
        self.queue.append(item)

    def remove(self):
        if self.queue:
           self.queue.pop(0)

    def check(self):
        return self.queue

q = Queue()

q.add("A")
q.add("B")
q.add("C")
q.add("D")
print(q.check())

q.remove()
q.remove()
print(q.check())