class Stack:
        def __init__(self):
            self.stack=[]
        def push(self,v):
              self.stack.append(v)
        def pop(self):
              self.stack.pop()
        def peek(self):
              return self.stack[-1]
        def isempty(self):
            return len(self.stack)==0
        def display(self):
              print(self.stack)


S=Stack()
S.push(10)
S.push(20)          
S.push(30)
S.display()
S.pop()
S.display() 



