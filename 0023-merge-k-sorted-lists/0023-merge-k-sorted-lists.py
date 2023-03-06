# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final = []
        for i in range(len(lists)):
            l = lists[i]
            while(l != None):
                final.append(l.val)
                l = l.next
        final = sorted(final)
        print(final)
        if len(final) == 0:
            return
        node = ListNode(final[0])
        fnode = node
        for i in range(1,len(final)):
            newnode = ListNode(final[i])
            node.next = newnode
            node = node.next
        return fnode