class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1={}
        d2={}
        b=0
        c=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                b+=1

            else:
                if secret[i] in d1:
                    d1[secret[i]]+=1
                else:
                    d1[secret[i]]=1

                if guess[i] in d2:
                    d2[guess[i]]+=1
                else:
                    d2[guess[i]]=1


        for j in range(0,10):
            j1=str(j)
            if j1 in d1 and j1 in d2:
                c+=min(d1[j1],d2[j1])


        res=str(b)+"A"+str(c)+"B"
        return res
            