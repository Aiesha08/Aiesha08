from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff=defaultdict(int)

        for char in s:
            diff[char]+=1
        for char in t:
            if diff[char] == 0:
                return char
            diff[char]-=1
        