class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class Binary_Search_Tree:
    def __init__(self,value=None):
        if value is None:
            self.head=None
        else:
            self.head=Node(value)

    def insert(self, value):
        if self.head:
            pointer=self.head
            parent=None
            while pointer:
                parent=pointer
                if pointer.value < value:
                    pointer=pointer.right
                else:
                    pointer=pointer.left
            if parent.value < value:
                parent.right=Node(value)
            else:
                parent.left=Node(value)
        else:
            self.head=Node(value)

    def print_tree(self):
        if self.head:
            pointer=self.head
            self.print_tree_helper(pointer)
        else:
            print("*")

    def print_tree_helper(self,pointer):
        if pointer:
            print(pointer.value)
            self.print_tree_helper(pointer.left)
            self.print_tree_helper(pointer.right)
        return

bst1=Binary_Search_Tree()
bst1.insert(12)
bst1.insert(24)
bst1.insert(10)
bst1.insert(18)

bst1.print_tree()