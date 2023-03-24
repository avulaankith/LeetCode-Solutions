#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		maxi = -1
		for i in arr:
		    maxi = max(maxi, i)
		secondmax = -1
		for i in arr:
		    if i == maxi:
		        continue
		    secondmax = max(secondmax, i)
		return secondmax


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends