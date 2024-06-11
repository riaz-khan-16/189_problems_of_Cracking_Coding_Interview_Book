
def pad(p,up):
    if not up:
        print(p)
        return 
    digit=int(up[0])
    
    for i in range((digit-1)*3,digit*3):
        ch=chr(ord('a')+i)
        pad(p+ch,up[1:])
 



pad('','')