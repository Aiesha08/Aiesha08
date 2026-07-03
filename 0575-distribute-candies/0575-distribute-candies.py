from collections import defaultdict
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can=defaultdict(int)
        t=len(candyType)/2

        for i in candyType:
            can[i]+=1
        if len(can) > t:
            return int(t)
        else: 
            return int(len(can))
        