# Nth Catalan Number

def catalan(n):
    dp=[0 for x in range(n+1)]
    dp[0],dp[1]=1,1
    for x in range(2,n+1):
        for y in range(x):
            dp[x]+=dp[y]*dp[x-y-1]
    return dp[n]