class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        totmins=[]
        for lv,level in enumerate(triangle):
            mins=[]
            if lv == 0:
                #print(level)
                mins.append(level[0])
            else: 
                for i, n in enumerate(level):
                    if i == 0:
                        #print(lv-1,i,totmins)
                        mins.append(totmins[lv-1][i]+n)
                    elif i == len(level)-1:
                        mins.append(totmins[lv-1][i-1]+n)
                    else:
                        mins.append(min(totmins[lv-1][i],totmins[lv-1][i-1])+n)
            totmins.append(mins)
        return min(totmins[-1])