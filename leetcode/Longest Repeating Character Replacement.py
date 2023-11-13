class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        left=0
        for right in range(0,len(s)):
            if s[right] in count:
                count[s[right]]=count[s[right]]+1
            else:
                count[s[right]]=1
            while (right-left+1)-max(count.values())>k:
                count[s[left]]=count[s[left]]-1
                left=left+1
            res=max(res,right-left+1)
        return res

