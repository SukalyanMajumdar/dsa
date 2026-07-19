class Node():
    def __init__(self,value=None,prev_elm=None,next_elm=None):
        self.value=value
        self.prev_elm=prev_elm
        self.next_elm=next_elm

class Doubly_Linked_List():
    def __init__(self, value=None):
        if value is None:
            self.head=self.tail=None
            self.length=0
        else:
            self.head=Node(value)
            self.tail=self.head
            self.length=1

    def printAll(self):
        pointer=self.head
        while pointer:
            print(pointer.value)
            pointer=pointer.next_elm

    def append(self,value):
        if self.length==0:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        else:
            newNode=Node(value,self.tail,None)
            self.tail.next_elm=newNode
            self.tail=newNode
        self.length+=1

    def pop(self):
        if self.length==0:
            return
        if self.length==1:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev_elm
            self.tail.next_elm=None
        self.length-=1

    def append_left(self,value): #Fix
        if self.length==0:
            self.append(value)
        else:
            newNode=Node(value,None,self.head)
            self.head.prev_elm=newNode
            self.head=newNode
            self.length+=1

    def pop_left(self): #Fix
        if (self.length==0) or (self.length==1):
            self.pop()
        else:
            self.head=self.head.next_elm
            self.head.prev_elm=None
            self.length-=1

dll1=Doubly_Linked_List()

dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")

dll1.append(8)

dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")

dll1.append(15)

dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")

dll1.append_left(2)
dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")

dll1.pop()
dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")

dll1.append_left(0)
dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")

dll1.pop_left()
dll1.printAll()
print("****")
print("length=",dll1.length)
print("****")