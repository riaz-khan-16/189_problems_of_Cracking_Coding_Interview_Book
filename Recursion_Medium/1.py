arr=[2,3,5,7]



def sum(a):
    s=0
    for i in a:
        s=s+i
    return s

def f(x):
    s=sum(x)
    for i in arr:
        if s+i==7:
            x.append(i)
            print(x)
            return 
        elif s+i<7:
             x.append(i)
             f(x)
             return
        else:
            return



for i in arr:
    x=[i]
    f(x)