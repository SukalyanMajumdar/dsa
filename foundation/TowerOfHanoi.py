# Tower of Hanoi
# no. of rods = 3 => A, B, C
disks=int(input("No. of disks (default 3): ") or 3)
print(disks)

def hanoi(source, via, target, disks):
    if disks==1: 
        print(f"{source} -> {target}")
        return
    else:
        hanoi(source, target, via, disks - 1) # sending everything above last disk to 'via', using 'target'
        print(f"{source} -> {target}") # sending last disk to 'target'
        hanoi(via, source, target, disks - 1) # sending everything at 'via' to 'target'
        
hanoi("A","B","C",disks)