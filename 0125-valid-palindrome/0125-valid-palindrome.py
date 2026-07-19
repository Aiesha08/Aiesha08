class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s=="" or s==" ":
            return True
        ans=""
        

        for ch in s:
            if ch.isalnum():
                ans += ch.lower()

        return ans == ans[::-1]