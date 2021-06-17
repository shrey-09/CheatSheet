# Edit Distance

h={}
def editDistance_TopDown(s1,s2):
    if (s1,s2) in h.keys():
        return h[(s1,s2)]
    if s1==s2:
        return 0
    elif len(s2)==0:
        return len(s1)
    else:
        if len(s1)==0: # You can only perform add operation when source string is of length 0
            return solve(s1,s2[1:]) + 1
        elif s1[0]==s2[0]: 
            return solve(s1[1:],s2[1:]) # Ignore
        else:
            a=solve(s1[1:],s2[1:]) + 1  # Replace
            b=solve(s1,s2[1:]) + 1      # Add
            c=solve(s1[1:],s2) + 1      # Delete
            h[(s1,s2)]= min([a,b,c])
            return h[(s1,s2)]

def editDistance_BottomUp(s, t):
    dp=[[0 for x in range(len(t)+1)] for y in range(len(s)+1)]
    for x in range(len(t)+1):
        dp[0][x]=x
    for x in range(len(s)+1):
        dp[x][0]=x
    for x in range(1,len(s)+1):
        for y in range(1,len(t)+1):
            if s[x-1]==t[y-1]:
                dp[x][y]=dp[x-1][y-1]
            else:
                dp[x][y]=min([dp[x-1][y-1],dp[x-1][y],dp[x][y-1]]) + 1
    return dp[len(s)][len(t)]