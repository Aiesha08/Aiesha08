class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=self.tonum(a)+self.tonum(b)
        s=self.tobinary(ans)
        return s
        


    def tonum(self,a:str)->int:
        sum=0
        t=len(a)-1
        for j in range(len(a)):
            sum=sum+(int(a[t])*(2**j))
            t-=1
        return sum
    def tobinary(self,n:int)->str:
        c=""
        if n==0:
            return "0"
        while n>0:
            r=n%2
            c=str(r)+c
            n=n//2
        return c
    


        