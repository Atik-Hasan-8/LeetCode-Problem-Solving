# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        turtle=head
        hear=head
        container=head
        
        while hear and hear.next:
            turtle=turtle.next
            hear=hear.next.next
            
        prev=None
        count=0
        while turtle:
            temp=turtle
            turtle=turtle.next
            temp.next=prev
            prev=temp
            count+=1
        count2=0
        ans=0
        while head and prev:
            res=head.val+prev.val
            ans=max(res,ans)
            if count==count2:
                break
            head=head.next
            prev=prev.next
            count2+=1
        return ans
        
        
        