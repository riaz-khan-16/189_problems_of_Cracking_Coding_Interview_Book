n=12
possible_squares=[]

for i in range(1,n):
    if i*i<n:
        possible_squares.append(i*i)
print(possible_squares)        


def f(x,c,possible_squares):
    if x==0:
        l=[]
        l.append(c)
        return l
    if x<0:
        l=[]
        return l
    li=[]
    for i in possible_squares:
        li= li+f(x-i,c+1,possible_squares)
        
    return li 

ans=f(12,0,possible_squares)       
print(ans)
