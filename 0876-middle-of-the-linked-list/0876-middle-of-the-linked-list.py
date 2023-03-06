# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # tortoise-hare approach
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # naive Solution
        # currN = head
        # n = 0

        # while(currN):
        #     n += 1
        #     currN = currN.next
        
        # mid = n // 2
        # currN = head
        # for i in range(mid):
        #     currN = currN.next
        # return currN