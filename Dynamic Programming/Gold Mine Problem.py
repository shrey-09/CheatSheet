# Gold Mine Problem

def goldMine(grid):
    n,m=len(grid),len(grid[0])
    dp=[[0 for x in range(m)] for y in range(n)]
    for x in range(n):
        dp[x][m-1]=grid[x][m-1]
    for y in range(m-2,-1,-1):
        for x in range(n):
            if x==0:
                dp[x][y]=max(dp[x][y+1],dp[x+1][y+1])+grid[x][y]
            elif x==n-1:
                dp[x][y]=max(dp[x][y+1],dp[x-1][y+1])+grid[x][y]
            else:
                dp[x][y]=max([dp[x][y+1],dp[x+1][y+1],dp[x-1][y+1]])+grid[x][y]
    ans=0
    for x in range(n):
        ans=max(ans,dp[x][0])
    return ans

grid=[
        [0,1,4,2,8,2],
        [4,3,6,5,0,1],
        [1,2,4,1,4,6],
        [2,0,7,3,2,2],
        [3,1,5,9,2,4],
        [2,7,0,8,5,1]
    ]
print(goldMine(grid))