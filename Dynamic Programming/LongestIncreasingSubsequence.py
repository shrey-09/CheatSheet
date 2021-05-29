# Longest Increasing Subsequence

# O (N^2) solution :
def LIS(arr):
    ans=[1 for x in range(len(arr))]
    for x in range(1,len(arr)):
        for y in range(0,x):
            if arr[x]>arr[y]:
                ans[x]=max(ans[x],ans[y]+1)
    return max(ans)

# O(N*LogN) solution:
def binarySearch(dp,target):
    start,end,possibleAns=0,len(dp)-1,len(dp)
    while start<=end:
        mid=(start+end)//2
        if dp[mid]==target:
            return mid
        elif dp[mid]>target:
            possibleAns=min(possibleAns,mid)
            end=mid-1
        elif dp[mid]<target:
            start=mid+1
    return possibleAns

def LIS_better(arr):
    dp=[arr[0]]
    for x in range(1,len(arr)):
        i=binarySearch(dp,arr[x])
        if i==len(dp):
            dp.append(arr[x])
        else:
            dp[i]=arr[x]
    return len(dp)
