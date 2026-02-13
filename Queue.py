class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,v):
        self.queue.append(v)
    def is_empty(self):
        return len(self.queue)==0
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    def display(self):
        print(self.queue)

Q=Queue()
Q.enqueue(10)
Q.enqueue(20)       
Q.enqueue(30)
Q.display()
Q.dequeue()
Q.display()