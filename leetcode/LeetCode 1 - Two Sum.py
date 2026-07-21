# Copy from Leetcode terminal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique_map={}
        for idx,elm in enumerate(nums):
            if elm not in unique_map:
                unique_map[target-elm]=idx
            else:
                return [unique_map[elm],idx]

'''
Notes:
the algorithm is to keep checking if the remainder aka (target-elm) is present in the hashmap. 
if not found, we store the index of remainder; if found we return current index and hashmap's remainder's index
for [3,3], 6 solution, in iteration 1, we do not find anything, thus we store it.
on iteration 2, current index is 1, but we find remainder's index at 0, we respond [1,0] (since one unique solutions only)
'''