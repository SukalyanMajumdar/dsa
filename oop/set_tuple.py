set1 = set() # make empty set using set(), using {} creates empty dictionary

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(1)
set1.add(5)

print(set1)

set1.remove(1)

print(set1)

try:
    set1.remove(69)
except Exception as e1:
    print("Exception raised:", e1)
finally:
    print(set1)
    
tuple1 = (1,2,3,1,5,True, "Yep", -300, 420.69)

try:
    tuple1.add(0)
except Exception as e2:
    print("Exception raised:", e2)
finally:
    print(tuple1)
    
try:
    tuple1.remove(1)
except Exception as e3:
    print("Exception raised:", e3)
finally:
    print(tuple1)    
