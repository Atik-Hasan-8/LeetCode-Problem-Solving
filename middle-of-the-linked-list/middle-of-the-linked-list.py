# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle=head
        hear=head
        
        while hear and hear.next:
            turtle=turtle.next
            hear=hear.next.next
            
        return turtle

        