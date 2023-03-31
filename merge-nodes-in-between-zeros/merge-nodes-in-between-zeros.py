# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        container=result
        num=0
        dump=head.next
        while dump:
            if dump.val==0:
                container.next=ListNode(num,container.next)
                container=container.next
                num=0
            num+=dump.val
            dump=dump.next
        return result.next
                
                
            
        