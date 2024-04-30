#here we will not take global array. we will create it in every function




#linear search example: find target element indices 

arr=[1,2,3,3,3,5,5,3]
target=3

def search(target, arr,index):
    l=[]
    if index>len(arr)-1:
        return l  

    if target==arr[index]:
        l.append(index)  
    x=search(target, arr,index+1)  
    return l+x

print(search(target, arr,0) )      

