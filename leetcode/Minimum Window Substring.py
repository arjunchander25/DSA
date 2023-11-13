class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        s_count={}
        t_count={}
        for i in range(0,len(t)):
            if t[i] in t_count:
                t_count[t[i]]=t_count[t[i]]+1
            else:
                t_count[t[i]]=1
        have,need=0,len(t_count)
        res,res_len='',float('infinity')
        for right in range(0,len(s)):
            if s[right] in s_count:
                s_count[s[right]]=s_count[s[right]]+1
            else:
                s_count[s[right]]=1

            if s[right] in t_count and t_count[s[right]]==s_count[s[right]]:
                have=have+1
            while have==need:
                if res_len>right-left+1:
                    res=s[left:right+1]
                    res_len=right-left+1
                s_count[s[left]]=s_count[s[left]]-1
                if s[left] in t_count and s_count[s[left]]<t_count[s[left]]:
                    have=have-1
                left=left+1
        if res_len==float('infinity'):
            return ''
        return res
            
