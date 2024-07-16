A='bd'
B='abcd'

def dp(i,j):

    if i>len(A)-1 or j>len(B)-1:
        return 0
    elif A[i]==B[j]:
        return 1+dp(i+1,j+1)
    else:
        return max(dp(i+1,j),dp(i,j+1))

print(dp(0,0))