
s="tree"
all=set()
for i in s:
  all.add(i)
 
d=[]
for k in all:
  d.append([k,s.count(k)])


def myf(x):
  return x[1]
d.sort(key=myf,reverse=True)


for i in range(len(d)):
  d[i]=d[i][0]*d[i][1]
  
print(''.join(d))  
