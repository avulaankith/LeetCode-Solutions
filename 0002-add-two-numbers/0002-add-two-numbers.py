# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        num1rev = ""
        num2rev = ""
        while(curr1!=None):
            num1rev = num1rev + str(curr1.val)
            curr1 = curr1.next
        while(curr2!=None):
            num2rev = num2rev + str(curr2.val)
            curr2 = curr2.next
        num1 = num1rev[::-1]
        num2 = num2rev[::-1]
        if len(num1) >= len(num2):
            curr = l1
        else:
            curr = l2
        s = int(num1)+int(num2)
        s = str(s)
        ls = []
        for i in range(len(s)):
            ls.append(s[i])
        # s = s[::-1]
        # print(ls)
        
        # curr = l1
        # count = 0
        head = ListNode()
        returnValue = head
        while(len(ls)!=0):
            head.val = ls[-1]
            ls.pop(-1)
            if len(ls) == 0:
                break
            new_node = ListNode()
            head.next = new_node
            head = head.next
        
        # while(curr!=None):
        #     curr.val = ls[-1]
        #     ls.pop(-1)
        #     # count+=1
        #     while len(ls) > 1 and curr.next == None:
        #         new_node = ListNode(ls[-1])
        #         ls.pop(-1)
        #         curr.next = new_node
        #         curr = curr.next
        #     curr = curr.next
        return returnValue