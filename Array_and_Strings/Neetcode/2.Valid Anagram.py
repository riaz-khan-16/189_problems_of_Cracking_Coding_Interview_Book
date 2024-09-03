# https://leetcode.com/problems/valid-anagram/description/

def solution(s,t):
    hashs={}
    x=set(s)
    for i in x:
        hashs[i]=s.count(i)
    y=set(t)
    hasht={}
    for i in y:
        hasht[i]=t.count(i)
    for k in x:
        if k not in y:
            return False
        if hashs[k]!=hasht[k]:
            return False
    if len(y)!=len(x):
            return False
    return True
s='a'
t='ab'
print(solution(s,t))