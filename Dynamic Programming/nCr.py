# Binomial Coefficient Problem (nCr)

def nCr(n, r):
    dp=[[0 for y in range(r+1)] for x in range(n+1)]
    for x in range(n+1):
        for y in range(min(x,r)+1): #min is used, when n<r there is no possible way to choose so it's 0.
            if y==0 or x==y:
                dp[x][y]=1
            else:
                dp[x][y]=dp[x-1][y]+dp[x-1][y-1]
    return dp[n][r]%1000000007
