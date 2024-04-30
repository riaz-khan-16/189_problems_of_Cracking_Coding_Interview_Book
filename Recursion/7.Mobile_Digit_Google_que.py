


def pad(p,up):
    if not up:
        l=[]
        l.append(p)
        return l
    digit=int(up[0])
    li=[]
    for i in range((digit-1)*3,digit*3):
        ch=chr(ord('a')+i)
        li=li+pad(p+ch,up[1:])
    return li 

print(pad('','23'))
