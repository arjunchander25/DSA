class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        res=0
        left=0
        right=0
        while right<len(s):
            if s[right] not in char:
                char.add(s[right])
                res=max(res,right-left+1)
            else:
                while s[right] in char:
                    char.remove(s[left])
                    left=left+1
                char.add(s[right])
            right=right+1
        return res
                
