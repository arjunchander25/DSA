class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res=[]
        res2=[]
        for i in range(0,len(s)):
            res.append(s[i])
        for j in range(0,len(t)):
            res2.append(t[j])
        res.sort()
        res2.sort()
        if res==res2:
            return True
        else:
            return False



        
