
s = ["h","e","l","l","o"]
def reverse(p,up):
            if not up:
                    return p
            x=[up[0]]
            p=x+p

            return reverse(p,up[1:])
            
x=reverse([],s)
print(x)