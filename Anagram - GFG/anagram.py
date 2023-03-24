#User function Template for python3

from collections import Counter
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        dict_a, dict_b = Counter(a), Counter(b)
        if dict_a == dict_b:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends