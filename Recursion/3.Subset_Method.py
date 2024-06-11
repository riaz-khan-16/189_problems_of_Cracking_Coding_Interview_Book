
sub=[]
def findAllSubsets(p,up):
    if not up:
        sub.append(p)
        return
    findAllSubsets(p+up[0],up[1:])
    findAllSubsets(p,up[1:])


findAllSubsets('','abc')  
print(sub)





    