# Copy from Leetcode terminal
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map={"(":")", "{":"}", "[":"]"}
        stack=[]
        for elm in s:
            if len(stack)>0 and brackets_map.get(stack[-1], None)==elm:
                stack.pop()
            else:
                stack.append(elm)
        if len(stack)==0:
            return True
        else:
            return False
