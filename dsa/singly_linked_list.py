class Node():
    def __init__(self,value,next_elm=None):
        self.value=value
        self.next_elm=next_elm

class Singly_Linked_List():
    def __init__(self,value=None):
        self.exists=Node(None,None)
        if value is None:
            self.head=self.tail=None
            self.length=0
        else:
            self.head=self.tail=Node(value)
            self.length=1

    def append(self, value):
        if self.length==0:
            self.tail=self.head=Node(value)
        else:
            self.tail.next_elm=Node(value)
            self.tail=self.tail.next_elm
        self.length+=1

    def printAll(self):
        pointer=self.head
        while pointer:
            print(pointer.value)
            pointer=pointer.next_elm

    def pop(self):
        if self.length==0:
            return
        if self.length==1:
            self.tail=self.head=None
            self.length=0
        else:
            pointer=self.head
            while pointer.next_elm.next_elm:
                pointer=pointer.next_elm
            pointer.next_elm=None
            self.tail=pointer
            self.length-=1

    def append_left(self,value):
        if self.length==0:
            self.append(value)
        else:
            temp_right_side=self.head
            self.head=Node(value,temp_right_side)
            self.length+=1

    def pop_left(self):
        if self.length==0:
            return
        if self.length==1:
            self.head=self.tail=None
            self.length=0
        else:
            self.head=self.head.next_elm
            self.length-=1

sll1=Singly_Linked_List(3)

sll1.append(5)

sll1.append(7)

sll1.append(10)

sll1.printAll()
print("****")
print("length=",sll1.length)
print("****")

sll1.pop()

sll1.printAll()
print("****")
print("length=",sll1.length)
print("****")

sll1.append_left(-200)

sll1.printAll()
print("****")
print("length=",sll1.length)
print("****")

sll1.pop_left()
sll1.printAll()
print("****")
print("length=",sll1.length)
print("****")