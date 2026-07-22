class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits) - 1, -1, -1):
            if (digits[idx]+1)==10:
                digits[idx]=0
            else:
                digits[idx]+=1
                break
        if digits[0]==0:
            return [1]+digits
        else:
            return digits
'''
Notes:
iterating from the other side of the list.
if the digit is 9, we make it 0
otherwise we add 1 to it and break the list.
if the 0th digit is 0, we append [1] with the list and return the list
'''        