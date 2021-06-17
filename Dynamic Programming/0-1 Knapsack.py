# 0-1 Knapsack

def knapSack(w, wt, val, n):
    dp=[[0 for x in range(w+1)] for y in range(n+1)]
    for x in range(1,n+1):
        for y in range(1,w+1):
            if wt[x-1]>y:
                dp[x][y]=dp[x-1][y]
            else:
                dp[x][y]=max(dp[x-1][y-wt[x-1]]+val[x-1],dp[x-1][y])
    return dp[n][w]