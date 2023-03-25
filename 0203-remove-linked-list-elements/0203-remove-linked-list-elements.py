# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return None

        prev = None
        curr = head
        while curr:
            if curr.val == val and prev:
                prev.next = curr.next
                curr = curr.next
                continue
            elif curr.val == val and not prev:
                head = head.next
                curr = curr.next
                continue
            prev = curr
            curr = curr.next
        
        return head