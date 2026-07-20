def merge(list1,list2):
    joined_list=[]
    total_joins=len(list1)+len(list2)
    i=0
    list1_i=0
    list2_i=0
    while (list1_i+list2_i)<total_joins:
        if list1_i==len(list1): # joining remaining list
            joined_list.append(list2[list2_i])
            list2_i+=1
        elif list2_i==len(list2): # joining remaining list
            joined_list.append(list1[list1_i])
            list1_i+=1
        else: # ideally the comparison should be first, not in else. but if an index reaches length, the list is not accessible anymore.
            if list1[list1_i] <= list2[list2_i]: # comparing and joining to main list. also used <= rather than < ,so that it will not change values if both are same. no functional impact, but more 'stable' and does 1 less operation.
                joined_list.append(list1[list1_i])
                list1_i+=1
            else:
                joined_list.append(list2[list2_i])
                list2_i+=1
    return joined_list

def split(list_input):
    list1=[]
    list2=[]
    midpoint = len(list_input)//2
    for elm in range(midpoint):
        list1.append(list_input[elm])
    for elm in range(midpoint,len(list_input)):
        list2.append(list_input[elm])
    return list1, list2

def merge_sort(input_list):
    if len(input_list)<=1:
        return input_list
    else:
        left_side,right_side=split(input_list)
        left_side=merge_sort(left_side)
        right_side=merge_sort(right_side)
        return merge(left_side,right_side)

print(merge_sort([-1,0,-5,-11,2,-3]))
print(merge_sort([1]))
print(merge_sort([]))