arr=[1,2,3,4,6,8]

sum_of_arr=0
for i in arr:
    sum_of_arr+=i
half_of_sum=   sum_of_arr//2
print(half_of_sum)

def subset_sum(p,up,s):
    if not up:
        return
    if s==half_of_sum:
        print(p)
    subset_sum(p+[up[0]],up[1:],s+up[0])    
    subset_sum(p,up[1:],s) 
       

subset_sum([],arr,0)