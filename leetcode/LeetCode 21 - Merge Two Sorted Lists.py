# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from dsa.foundation.dict import temp


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final_list=ListNode(None,None)
        pointer=final_list
        while list1 and list2:
            if list1.val<=list2.val:
                pointer.next=list1
                list1=list1.next
            else:
                pointer.next=list2
                list2=list2.next
            pointer=pointer.next
        if list1:
            pointer.next=list1
        if list2:
            pointer.next=list2
        return final_list.next

'''
Notes:
i made a list node as None and made a pointer point to it (step 0). now if each of the list exists, i check both lists and select the lower one. once selected, append that whole list to my pointer's next and push the list one step (step 1). once any of the list empties, i append the other list at pointer (step 2). once done i return temp list .next(since the list starts as None and we dont want that.) (step 3)

step 0:
final_list = Node(None,None)
pointer -> final_list

(ex: merging 1->2->4 and 1->3->4)

step 1:
1(a)->2->4(a)  [a and b to determine if its from list 1 or list2, nothing else]
1(b)->3->4(b)

1(a)<1(b):
pointer -> 1(a)->2->4(a)
pointer -> pointer.next
1(a)->2->4(a) --> 2->4(a)

next iteration:
1(b)<2:
pointer -> 1(a) -> 1(b)->3->4(b)
pointer -> pointer.next
1(b)->3->4(b) --> 3->4(b)

next iteration:
2<3:
pointer -> 1(a) -> 1(b) -> 2->4(a)
pointer -> pointer.next
2->4(a) --> 4(a)

next iteration:
3<4(a):
pointer -> 1(a) -> 1(b) -> 2 -> 3->(4b)
pointer -> pointer.next
3->4(b) -> 4(b)

next iteration:
4(a)<4b:
pointer -> 1(a) -> 1(b) -> 2 -> 3 -> 4(a)
pointer -> pointer.next
4(a) -> None

list1 empties, while loop breaks

step 2:
merging remaining list2:

pointer -> 4(b)

step 3:
the final list is built like this now: 
None -> 1(a) -> 1(b) -> 2 -> 3 -> 4(a) -> 4(b)

returning final_list.next
'''