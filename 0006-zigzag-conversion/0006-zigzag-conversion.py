class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        t=[[] for _ in range(numRows)]
        

        
        cycle = 2 * numRows - 2

        for j in range(len(s)):
            pos = j % cycle

            if pos < numRows:
                row = pos
            else:
                row = cycle - pos

            t[row].append(s[j])
        ans = ""
        for row in t:
            ans += "".join(row)

        return ans