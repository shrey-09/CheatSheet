# Minimum number of operations required to make
# String1 equal to String2 by using following operations with their cost:
#   Ignore: Costs 0
#   Add: Costs 1
#   Replace: Costs 1
#   Delete: Costs 1

h={}
def solve(s1,s2):
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

print(solve("sunday","saturday"))