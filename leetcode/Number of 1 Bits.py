class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n!=0:
            if (n%10)%2==1:
                res=res+1
            n=n>>1
        return res
        
        
