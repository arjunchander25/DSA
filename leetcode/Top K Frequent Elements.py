class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for num in nums:
            if num in res:
                res[num]=res[num]+1
            else:
                res[num]=1
        sorted_dict = {key: val for key, val in sorted(res.items(), key=lambda item: item[1], reverse=True)}

        res2=[]
        for i in sorted_dict:
            res2.append(i)
            k=k-1
            if k==0:
                break
        return res2
    
            
            
        
            
        
