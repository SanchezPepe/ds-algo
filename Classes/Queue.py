class Queue():
    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.append(data)
    
    def dequeue(self):
        size = len(self.data)
        if self.isEmpty():
            print(self.data, "Queue is empty")
            return None
        else:
            return self.data.pop(0)
    
    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data

    def printq(self):
        print(self.data)


q = Queue()

for i in range(10):
    q.enqueue(i)

q.printq()

for i in range(5):
    item = q.dequeue()

q.printq()
