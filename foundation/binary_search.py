def binary_search(input_list,target,start_index,end_index):
    middle=(end_index+start_index)//2
    if start_index > end_index:
        print(f"{target} not present in list {input_list}")
        return None
    elif input_list[middle]==target:
        print(f"{target} Found at index {middle} in list {input_list}")
        return middle
    elif input_list[middle] > target:
        return binary_search(input_list,target,start_index,middle-1)
    elif input_list[middle] < target:
        return binary_search(input_list,target,middle+1,end_index)

binary_search([-11, -5, -3, -1, 0, 2],69,0,5)