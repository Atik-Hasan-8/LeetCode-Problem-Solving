# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left_node=head
        right_node=head
        
        for i in range(k-1):
            left_node=left_node.next
        
        tail=left_node
        while tail.next:
            right_node=right_node.next
            tail=tail.next
            
        left_node.val,right_node.val=right_node.val,left_node.val
        
        
        return head