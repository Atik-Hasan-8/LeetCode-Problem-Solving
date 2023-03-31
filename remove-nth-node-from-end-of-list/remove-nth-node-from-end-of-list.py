# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right=head
        dummy=ListNode(0,head)
        left=dummy
        while n>0 and right:
            right=right.next
            n-=1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next

        
        