# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        count = 0
        while(node != None):
            count += 1
            node = node.next
        if count == n:
            return head.next
        if count == 1:
            return None
        m = count - n
        ptr = head
        for i in range(1,m):
            ptr = ptr.next
        
        ptr.next = ptr.next.next
        return head