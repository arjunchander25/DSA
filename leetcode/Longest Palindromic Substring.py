class Solution:
    def longestPalindrome(self, s: str) -> str:
        res={}
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    length=len(s[i:j])
                    res[length]=s[i:j]
        return res[max(res.keys())]

        
    
    def palin(self,x):
        left=0
        right=len(x)-1
        while left<=right:
            if x[left]==x[right]:
                right=right-1
                left=left+1
            else:
                return False
        return True
        
