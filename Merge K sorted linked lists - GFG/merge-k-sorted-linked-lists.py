#User function Template for python3
'''
	Your task is to merge the given k sorted
	linked lists into one list and return
	the the new formed linked list class.

	Function Arguments:
	    arr is a list containing the n linkedlist head pointers
	    n is an integer value
    
    node class:
    
class Node:
    def __init__(self,x):
        self.data = x
        self.nxt = None
'''
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        # return head of merged list
        if K == 1:
            return arr[0]
            
        # def merge(a, b):
        #     lis = []
        #     n = len(a)
        #     m = len(b)
        #     i = 0
        #     j = 0
        #     while(i < n and j < m):
        #         if a[i] < b[j]:
        #             lis.append(a[i])
        #             i += 1
        #         else:
        #             lis.append(b[j])
        #             j += 1
        #     if i < n:
        #         lis.extend(a[i:])
        #     elif j < m:
        #         lis.extend(b[j:])

        #     return lis
        
        lis = []
        for i in range(K):
            node = arr[i]
            while(node):
                lis.append(node.data)
                node = node.next
    
        lis = sorted(lis)
        
        head = Node(lis[0])
        node = head
        for i in lis[1:]:
            node.next = Node(i)
            node = node.next
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends