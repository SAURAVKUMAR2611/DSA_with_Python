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
    

    
