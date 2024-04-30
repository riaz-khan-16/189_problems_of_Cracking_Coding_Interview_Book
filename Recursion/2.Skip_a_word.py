

s='acndkapplefhkd'
target='apple'

def skipApple(ans,s):
    if not s:
        return ans
    if s[0:len(target)]==target:
        ans=ans+''
        return skipApple(ans,s[len(target):])
    else:
        ans=ans+s[0]
        return skipApple(ans, s[1:])

print(skipApple('',s))

