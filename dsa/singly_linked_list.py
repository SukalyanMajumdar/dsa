class Node():
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class SinglyLinkedList():
    def __init__(self, value=None):
        self.head=Node(None,None)
        if value is None:
            self.tail=self.head
            self.length=0            
        else:
            self.tail=Node(value,None)
            self.head.next=self.tail
            self.length=1
                    
    def append(self, value):
        self.tail.next=Node(value)
        self.tail=self.tail.next
        self.length+=1
        
    def pop(self):
        if self.length>0:
            iteration=0
            pointer=self.head
            while iteration<self.length-1:
                iteration+=1
                pointer=pointer.next
            pointer.next=None
            self.tail=pointer
            self.length-=1
            
    def append_left(self, value):
        if self.length>0:
            temp=self.head.next
            self.head.next=Node(value,temp)
        else:
            self.tail=Node(value)
            self.head.next=self.tail
        self.length+=1
        
    def pop_left(self):
        if self.length==1:
            self.head.next=None
            self.tail=self.head
            self.length-=1
        elif self.length>1:
            self.head.next=self.head.next.next
            self.length-=1
                                                
linkedlist1=SinglyLinkedList()