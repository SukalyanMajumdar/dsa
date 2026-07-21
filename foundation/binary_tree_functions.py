# class TreeNode: # type: ignore
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def height(node):
#     if node:
#         current_height=1
#         left_height = height(node.left)
#         right_height = height(node.right)
#         return current_height+max(left_height,right_height)
#     else:
#         return 0
    
# def diameter(node,local_max=0):
#     if node:
#         local_max = height(node.left)+height(node.right)
#         local_max = max(diameter(node.left), diameter(node.right), local_max)
#     return local_max

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# root = TreeNode(1)

# # Level 1
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# # # Level 2
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# root.right.right = TreeNode(6)

# # Level 3
# root.left.left.left = TreeNode(20)
# root.left.left.right = TreeNode(100)

# root.right.right.left = TreeNode(8)
# root.right.right.right = TreeNode(7)

# # Level 4
# root.left.left.right.left = TreeNode(70)

# root.right.right.left.left = TreeNode(200)
# root.right.right.left.right = TreeNode(9)

# root.right.right.right.left = TreeNode(11)
# root.right.right.right.right = TreeNode(15)

# # Level 5
# root.right.right.left.right.left = TreeNode(10)

# root.right.right.right.left.right = TreeNode(12)

# # Level 6
# root.right.right.left.right.left.left = TreeNode(500)
# root.right.right.left.right.left.right = TreeNode(25)

# print(height(root))

# print(diameter(root))