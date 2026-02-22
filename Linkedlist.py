class Node:
    def __init__(self,v):
        self.value=v
        self.next=None
        return
    def isempty(self):
        return self.value==None
    def append(self,v):
        if self.value==None:
            self.value=v
        else:
            temp=self
            while temp.next!=None:
                temp = temp.next
            temp.next=Node(v)
        return
    
    def display(self):
        temp=self
        while temp!=None:
            print(temp.value,end="-> ")
            temp = temp.next
        print()
        return
    def Length(self):
        temp= self
        count =0
        while temp != None:
            count +=1
            temp = temp.next
        return count
    
    def insert (self,v,pos):
        if pos==0:
            newnode=Node(v)
            newnode.next=self
            return newnode
        else:
            temp=self
            count=0
            while temp!=None and count<pos-1:
                temp = temp.next
                count +=1               
            if temp==None:
                print("position out of bound")      
            else:
                newnode=Node(v)
                newnode.next=temp.next
                temp.next=newnode 
            return self
        
    def delete(self,pos):
        if pos==0:
            return self.next
        else:
            temp = self
            count=0
            while temp!=None and count<pos-1:
                temp = temp.next
                count +=1
            if temp==None or temp.next==None:
                print("position out of bound")
            else:       
                temp.next = temp.next.next
            return self
            
    
l=Node(None)
l.append(1) 
l.append(2)
l.append(3)    
l.insert(8,2)  
l.delete(2)       
l.display()
print(l.Length())   
    
#Finding Middle of the Linkedlist
def find_middle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.value

#Reverse a Linkedlist
def iterative_revrse(head):
    prev=None
    current=head
    while current!=None:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev
    

iterative_revrse(l).display()

def recursive_reverse(head):
    if head==None or head.next==None:
        return head
    new_head=recursive_reverse(head.next)
    head.next.next=head
    head.next=None
    return new_head


#Detecting a Cycle in a Linkedlist
def hasCycle(head):
    visited = set()
    temp = head
    while temp != None:
        if temp in visited:
            return True 
        visited.add(temp)
        temp = temp.next
    return False

def starting_of_cycle(head):
    slow = head
    fast = head
    while fast !=None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.value
    return None