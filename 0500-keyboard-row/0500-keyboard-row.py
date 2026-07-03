class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard={1:"qwertyuiop",2:"asdfghjkl",3:"zxcvbnm"}
        ans=[]
        c=0

        for word in words:
            same=0
            c=0
            for char in word:
                if char.lower() in keyboard[1]:
                    if same!=0 and same!=1:

                        break
                    else:
                        same=1
                        c+=1
                if char.lower() in keyboard[2]:
                    if same!=0 and same!=2:
                        break
                    else:
                        same=2
                        c+=1
                if char.lower() in keyboard[3]:
                    if same!=0 and same!=3:
                        break 
                    else:
                        same=3
                        c+=1  
            if c==len(word):
                ans.append(word)
                

            

        return ans


        