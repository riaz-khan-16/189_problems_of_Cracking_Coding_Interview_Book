#https://leetcode.com/problems/subsets/description/


def f(p,up):
    
    if not up:
        print(p)
        return [p]
    p.append(up[0])
    f(p,up[1:])

    p.pop()
    f(p,up[1:])


f([],[1,2,2])    