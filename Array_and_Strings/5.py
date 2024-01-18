# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# Hints:#23, #97, #130


ori='pale'
new='bale'

def isremoved(ori,new):
    x=0
    for i in ori:
        if i not in new:
            x=x+1
    if x>1:
        return False
    else:
        return True        



def isinserted(ori,new):
    x=0
    for i in new:
        if i not in ori:
            x=x+1
    if x>1:
        return False
    else:
        return True  
    

def isreplaced(ori,new):
    x=0
    for i in range (len(new)):
        if ori[i] != new[i]:
            x=x+1
    if x>1:
        return False
    else:
        return True 
    


if len(ori)>len(new):    # it may be removed
    print(isremoved(ori,new))

elif len(ori)<len(new):  #may be inserted
    print(isinserted (ori,new))

elif len(ori)==len(new):
    print(isreplaced(ori,new))

else:
    print(False)      