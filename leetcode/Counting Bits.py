class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            count=0
            for j in range(0,len(bin(i)[2:])):
                if bin(i)[2:][j]=='1':
                    count=count+1
            res.append(count)
        return res
        
