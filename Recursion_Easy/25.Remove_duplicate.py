s= 'geeksforgeeks'

def f(p,up):
    if not up:
        print(p)
        return p
    x=up[0]
    if p:
        if p[-1]!=x:
            p=p+x
    f(p,up[1:])

f(s[0],s[1:])


