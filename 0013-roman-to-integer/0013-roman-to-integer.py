class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        stack={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        for i in range(len(s)):
            
            if i + 1 < len(s) and stack[s[i]] < stack[s[i+1]]:
                ans -= stack[s[i]]
            else:
                ans += stack[s[i]]

        return ans
        