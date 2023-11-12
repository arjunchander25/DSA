class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=len(arr)-2
        maxx=0
        while i>=0:
            maxx=max(arr[i+1],maxx)
            arr[i+1]=maxx
            i=i-1
        arr.append(-1)
        return arr[1:]
        #
        
