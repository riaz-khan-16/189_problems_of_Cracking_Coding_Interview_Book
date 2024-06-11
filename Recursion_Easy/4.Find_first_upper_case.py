x='geeksforgeeks'

def f(i,x):
    if i==len(x):
        return -1
    if x[i].isupper():
        return x[i]
    return f(i+1,x) 

print(f(0,x))