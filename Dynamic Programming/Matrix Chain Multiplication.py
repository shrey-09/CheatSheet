# Matrix Chain Multiplication

def mcm_Memo(arr):
    h={}
    def solve(i,j):
        if i==j:
            return 0
        else:
            if (i,j) in h.keys():
                return h[(i,j)]
            mini=float('inf')
            for k in range(i,j):
                current=solve(i,k)+solve(k+1,j)+arr[i-1]*arr[k]*arr[j]
                mini=min(mini,current)
            h[(i,j)]=mini
            return mini
    return solve(1,len(arr)-1)

def mcm_BottomUp(arr):
    n=len(arr)
    dp=[[0 for x in range(n+1)] for y in range(n+1)]
    for x in range(1,n):
        dp[x][x]=0
    
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            mini=float('inf')
            for k in range(i,j):
                prod=arr[i-1]*arr[k]*arr[j]
                mini=min(mini,dp[i][k]+dp[k+1][j]+prod)
            dp[i][j]=mini
    return dp[1][n-1]

print(mcm_Memo([1, 2, 3, 4,5]))
print(mcm_BottomUp([1,2,3,4,5]))