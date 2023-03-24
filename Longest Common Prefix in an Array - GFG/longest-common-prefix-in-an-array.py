#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        mini = 99999999
        for i in arr:
            mini = min(mini, len(i))
        
        k = 0
        st =""
        for i in range(mini):
            prev = arr[0][i]
            for j in arr[1:]:
                curr = j[i]
                if prev != curr:
                    if st == "":
                        return -1
                    return st
            else:
                st += prev
        if st == "":
            return -1
        return st
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends