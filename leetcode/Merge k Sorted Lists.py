class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists==[]:
            return None
        while len(lists)>1:
            res=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                if i+1<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None
                res.append(self.helper(l1,l2))
            lists=res
        return lists[0]
            




    def helper(self,l1,l2):
        dummy=ListNode()
        curr=dummy
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                curr.next=l1
                curr=curr.next
                l1=l1.next

            else:
                curr.next=l2
                curr=curr.next
                l2=l2.next
        if l1!=None:
            curr.next=l1
        if l2!=None:
            curr.next=l2

        return dummy.next

    





        
        
