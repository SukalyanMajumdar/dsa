list1= [1,2,"Three", False, 0.69, -420]
print(list1)

list1.append("something")
print(list1)

list1.insert(0, "something at front") # should avoid and use deque
print(list1)

############################################

from collections import deque

dq = deque([1,2,"Three", False, 0.69, -420])
print(dq)

dq.append("something at deque")
print(dq)

dq.appendleft("something at front at deque") # efficient ! should use this
print(dq)