s = "00110"
s = "010110"
s = "00011000"

memo={}
def recursive(index, mono):

    if index==len(s):
        return 0

    if (index, mono) in memo:
        return memo[(index, mono)]
    if mono and s[index]=='0':
        memo[(index, mono)]=min(1+recursive(index+1, mono=False), recursive(index+1, mono))
        return memo[(index, mono)]
    if mono and s[index]=='1':
        memo[(index, mono)]=min(1+recursive(index+1, mono), recursive(index+1, mono=False))
        return memo[(index, mono)]
    if not mono and s[index]=='1':
        memo[(index, mono)]=recursive(index+1, mono=False)
        return memo[(index, mono)]
    if not mono and s[index]=='0':
        memo[(index, mono)]=1+recursive(index+1, mono=False)
        return memo[(index, mono)]
    
print(recursive(0, mono=True))    
    


 
    
 
