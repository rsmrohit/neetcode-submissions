# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head

        if not head:
            return head

        if not head.next:
            return head

        target = head.next
        head.next = None
        
        while target.next:

            t1, t2, t3 = prev, target, target.next
            target.next = t1
            prev = t2
            target = t3

            

        target.next = prev
        return target
