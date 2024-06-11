n = 4
k = 11


def invert_and_reverse(st):
    x=''
    for i in range(len(st)):
        if st[i]=='0':
            x=x+'1'
        if st[i]=='1':
            x=x+'0'
        return st[::-1]       

def f(n):
    if n==1: return '0'
    return f(n-1)+'1'+invert_and_reverse(f(n-1))

x=f(n)
print(x[k-1])
