# Search in a Maze

ans=[]
def searchInMaze(grid,i,j,path):
    if i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='$' or grid[i][j]==0:
        return
    elif i==len(grid)-1 and j==len(grid[0])-1:
        ans.append(path)
        return
    grid[i][j]='$'
    searchInMaze(grid,i,j+1,path+'R')
    searchInMaze(grid,i,j-1,path+'L')
    searchInMaze(grid,i-1,j,path+'U')
    searchInMaze(grid,i+1,j,path+'D')
    grid[i][j]=1
    return

grid=[[1, 0, 0, 0],
      [1, 1, 0, 1], 
      [1, 1, 0, 0],
      [0, 1, 1, 1]]
searchInMaze(grid,0,0,"")
for x in ans:
    print(x,end=" ")