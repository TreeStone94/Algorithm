# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # 이전
        curr = head # 현재

        while curr: # 
            next_temp = curr.next # {node.val = 2, node.next = node(3)}, {node.val = 3, node.next = node(4)}
            curr.next = prev # None, {node.val = 1, node.next = None}
            prev = curr # prev = {node.val = 1, node.next = None}
            curr = next_temp 

        return prev
       
